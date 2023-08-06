import datetime
from enum import Enum
from typing import Dict, Optional, List, Union

from moviebotapi import Session
from moviebotapi.core import utils
from moviebotapi.core.basemodel import BaseModel


class CateLevel1(str, Enum):
    Movie = 'Movie'
    TV = 'TV'
    Documentary = 'Documentary'
    Anime = 'Anime'
    Music = 'Music'
    Game = 'Game'
    AV = 'AV'
    Other = 'Other'

    @staticmethod
    def get_type(enum_name: str) -> "CateLevel1":
        for item in CateLevel1:
            if item.name == enum_name:
                return item
        return


class TVSeries(BaseModel):
    season_start: int = None
    season_end: int = None
    season_full_index: List[int] = []
    ep_start: int = None
    ep_end: int = None
    ep_full_index: List[int] = []
    season_is_fill: bool = False
    ep_is_fill: bool = False
    contains_complete_ep: bool = False
    contains_complete_season: bool = False
    contains_multiple_season: bool = False

    def __init__(self, data: Optional[Dict] = None):
        utils.copy_value(data, self)


class Torrent(BaseModel):
    # 种子id
    id: str
    # 站点编号
    site_id: str
    gmt_modified: datetime.datetime
    # 种子编号
    # torrent_id: int = db.Column(db.Integer, nullable=False, primary_key=True, unique=True)
    # 种子名称
    name: str
    # 种子标题
    subject: str
    # 以及类目
    cate_level1: CateLevel1
    # 站点类目id
    cate_id: str
    # 种子详情页地址
    details_url: str
    # 种子下载链接
    download_url: str
    # 种子关联的imdbid
    imdb_id: str
    # 种子发布时间
    publish_date: datetime.datetime
    # 种子大小，转化为mb尺寸
    size_mb: float
    # 做种人数
    upload_count: int
    # 下载中人数
    downloading_count: int
    # 下载完成人数
    download_count: int
    # 免费截止时间
    free_deadline: datetime.datetime
    # 下载折扣，1为不免费
    download_volume_factor: float
    # 做种上传系数，1为正常
    upload_volume_factor: int
    minimum_ratio: float
    minimum_seed_time: int
    # 封面链接
    poster_url: str

    def __init__(self, data: Optional[Dict] = None):
        utils.copy_value(data, self)

    @staticmethod
    def build_by_parse_item(site_config, item):
        t = Torrent()
        t.site_id = utils.parse_value(str, site_config.get('id'))
        t.id = utils.parse_value(int, item.get('id'))
        t.name = utils.parse_value(str, item.get('title'))
        t.subject = utils.parse_value(str, item.get('description'), '')
        if t.subject:
            t.subject = t.subject.strip()
        t.free_deadline = utils.parse_value(datetime.datetime, item.get('free_deadline'))
        t.imdb_id = utils.parse_value(str, item.get('imdbid'))
        t.upload_count = utils.parse_value(int, item.get('seeders'), 0)
        t.downloading_count = utils.parse_value(int, item.get('leechers'), 0)
        t.download_count = utils.parse_value(int, item.get('grabs'), 0)
        t.download_url = utils.parse_value(str, item.get('download'))
        if t.download_url and not t.download_url.startswith('http'):
            t.download_url = site_config.get('domain') + t.download_url
        t.publish_date = utils.parse_value(datetime.datetime, item.get('date'), datetime.datetime.now())
        t.cate_id = utils.parse_value(str, item.get('category'))
        for c in site_config.get('category_mappings'):
            cid = t.cate_id
            id_mapping = site_config.get('category_id_mapping')
            if id_mapping:
                for mid in id_mapping:
                    if str(mid.get('id')) == str(cid):
                        if isinstance(mid.get('mapping'), list):
                            cid = mid.get('mapping')[0]
                        else:
                            cid = mid.get('mapping')
            if str(c.get('id')) == str(cid):
                t.cate_level1 = CateLevel1.get_type(c.get('cate_level1'))
        t.details_url = utils.parse_value(str, item.get('details'))
        if t.details_url:
            t.details_url = site_config.get('domain') + t.details_url
        t.download_volume_factor = utils.parse_value(float, item.get('downloadvolumefactor'), 1)
        t.upload_volume_factor = utils.parse_value(int, item.get('uploadvolumefactor'))
        t.size_mb = utils.trans_size_str_to_mb(utils.parse_value(str, item.get('size'), '0'))
        t.poster_url = utils.parse_value(str, item.get('poster'))
        t.minimum_ratio = utils.parse_value(float, item.get('minimumratio'), 0.0)
        t.minimum_seed_time = utils.parse_value(int, item.get('minimumseedtime'), 0)
        if t.poster_url:
            if t.poster_url.startswith("./"):
                t.poster_url = site_config.get('domain') + t.poster_url[2:]
            elif not t.poster_url.startswith("http"):
                t.poster_url = site_config.get('domain') + t.poster_url
        return t


class TorrentDetail(BaseModel):
    site_id: str = None
    name: str = None
    subject: str = None
    download_url: str = None
    filename: str = None
    intro: str = None
    publish_date: datetime.datetime = None

    @staticmethod
    def build(site_config, item):
        if not item:
            return
        t = TorrentDetail()
        t.site_id = site_config.get('id')
        t.id = utils.parse_value(int, item.get('id'))
        t.name = utils.parse_value(str, item.get('title'), '')
        t.subject = utils.parse_value(str, item.get('description'), '')
        if t.subject:
            t.subject = t.subject.strip()
        t.download_url = utils.parse_value(str, item.get('download'))
        if t.download_url and not t.download_url.startswith('http'):
            t.download_url = site_config.get('domain') + t.download_url
        t.filename = utils.parse_value(str, item.get('filename'))
        t.intro = utils.parse_value(str, item.get('intro'))
        t.publish_date = utils.parse_value(datetime.datetime, item.get('date'))
        return t


class SearchType(str, Enum):
    Keyword = 'keyword'
    Imdb = 'imdb_id'


class SearchQuery(BaseModel):
    key: SearchType
    value: str

    def __init__(self, key: SearchType, value: str):
        self.key = key
        self.value = value


class TrafficManagementStatus(int, Enum):
    Disabled = 0
    Initiative = 1
    Passive = 2


class SiteStatus(int, Enum):
    Normal = 1
    Error = 2


class Site(BaseModel):
    id: int
    gmt_modified: datetime.datetime
    uid: int
    username: str
    cookie: str
    web_search: bool
    smart_download: bool
    share_rate: float
    upload_size: float
    download_size: float
    is_vip: bool
    status: SiteStatus
    traffic_management_status: TrafficManagementStatus
    # 主动模式时上传流量目标，单位GB
    upload_kpi: int
    proxies: str
    user_agent: str
    domain: str

    def __init__(self, data: Dict, api: "SiteApi"):
        utils.copy_value(data, self)
        self.site_id: str = utils.parse_value(str, data.get('site_name'))
        self.site_name: str = utils.parse_value(str, data.get('alias'))
        self._api = api

    def update(self):
        self._api.update(self.site_id, self.cookie, self.web_search, self.smart_download,
                         self.traffic_management_status, self.upload_kpi, self.proxies, self.user_agent)

    def delete(self):
        self._api.delete(self.id)


class SiteUserinfo(BaseModel):
    uid: int
    username: str
    user_group: str
    share_ratio: float
    uploaded: float
    downloaded: float
    seeding: int
    leeching: int
    vip_group: bool = False


class SiteApi:
    def __init__(self, session: Session):
        self._session: Session = session

    def list(self):
        list_ = self._session.get('site.get_sites')
        if not list_:
            return
        return [Site(x, self) for x in list_]

    def update(self, site_id: str, cookie: str,
               web_search: Optional[bool] = None, smart_download: bool = None,
               traffic_management_status: Optional[TrafficManagementStatus] = None,
               upload_kpi: Optional[int] = None, proxies: Optional[str] = None,
               user_agent: Optional[str] = None):
        self._session.post('site.save_site', json={
            'site_name': site_id,
            'cookie': cookie,
            'web_search': web_search,
            'smart_download': smart_download,
            'traffic_management_status': traffic_management_status,
            'upload_kpi': upload_kpi,
            'proxies': proxies,
            'user_agent': user_agent
        })

    def delete(self, id_: int):
        self._session.post('site.delete', {
            'id': id_
        })

    def search_local(self, query: Union[SearchQuery, List[SearchQuery]],
                     cate_level1: Optional[List[CateLevel1]] = None) -> List[Torrent]:
        if isinstance(query, SearchQuery):
            query = [{'key': query.key.value, 'value': query.value}]
        elif isinstance(query, list):
            query = [{'key': str(x.key), 'value': x.value} for x in query]
        torrents = self._session.post('site.search_local', {
            'query': query,
            'cate_level1': cate_level1
        })
        if not torrents:
            return []
        return [Torrent(x) for x in torrents]

    def list_local_torrents(self, start_time: Optional[str] = None) -> List[Torrent]:
        """
        获取本地种子列表
        :param start_time:
        :return:
        """
        torrents = self._session.get('site.list_local_torrents', {
            'start_time': start_time
        })
        if not torrents:
            return []
        return [Torrent(x) for x in torrents]

    def search_remote(self, query: Union[SearchQuery, List[SearchQuery]],
                      cate_level1: Optional[List[CateLevel1]] = None, timeout: Optional[int] = 15,
                      site_id: Optional[List[str]] = None) -> List[Torrent]:
        if isinstance(query, SearchQuery):
            query = [{'key': query.key.value, 'value': query.value}]
        elif isinstance(query, list):
            query = [{'key': str(x.key), 'value': x.value} for x in query]
        torrents = self._session.post('site.search_remote', {
            'query': query,
            'cate_level1': cate_level1,
            'timeout': timeout,
            'site_id': site_id
        })
        if not torrents:
            return []
        return [Torrent(x) for x in torrents]


TorrentList = List[Torrent]
