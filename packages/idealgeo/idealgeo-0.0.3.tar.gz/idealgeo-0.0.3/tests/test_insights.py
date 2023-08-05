from idealgeo.insights import Insight

def test_insight():
    insight = Insight(
        id='test',
        name='test',
        version='1.0',
        description='test'
    )
    assert insight.id == 'test'
    assert insight.name == 'test'
    assert insight.version == '1.0'
    assert insight.description == 'test'
