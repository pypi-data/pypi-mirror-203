import os

import requests

class IdealSpotClient:
    '''Client for the IdealSpot API

    Parameters
    ----------
    token : str
    url : str, optional

    Attributes
    ----------
    token : str
    url : str
    _insights : list of Insight

    Methods
    -------
    insights()
    describe_insight(insight)
    query_insight(insight, locations, insight_opts=None)

    Examples
    --------
    >>> from idealgeo import IdealSpotClient
    >>> client = IdealSpotClient('my_api_token')
    >>> insights = client.insights()
    >>> for ins in insights:
    >>>   print(ins.name + ':', ins.description)

    '''

    def __init__(self, token, url='https://www.idealgeo.com/api/v1'):
        self.token = token
        self.url = url
        self._insights = None
        
    def insights(self):
        if self._insights:
            return self._insights
        url = os.path.join(self.url, 'data', 'insights')
        headers = dict(api_key=self.token)
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        d = r.json().get('data')
        self._insights = [Insight(**ins) for ins in d]
        return self._insights
    
    def describe_insight(self, insight):
        url = os.path.join(self.url, 'data', 'insights', insight.id)
        headers = dict(api_key=self.token)
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        return r.json().get('data')
    
    def query_insight(self, insight, locations, insight_opts=None):
        url = os.path.join(self.url, 'data', 'insights', insight.id, 'query')
        headers = dict(api_key=self.token)
        locations = [str(l) for l in locations]
        params = {
            "version": insight.version, 
            "location[]": locations
        }
        if insight_opts:
            params['opts'] = json.dumps(dict(data=insight_opts))
        r = requests.get(url, headers=headers, params=params)
        r.raise_for_status()
        return r.json().get('data')

