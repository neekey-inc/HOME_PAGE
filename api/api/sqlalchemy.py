from api import settings

import sqlalchemy.orm

from sqlalchemy.engine.url import URL

def db_url():
    db_settings = settings.DATABASES['default']
    url = URL(drivername=settings.DATABASE_ENGINE,
        database=db_settings['homepagedb'],
        username=db_settings['neekey'],
        password=db_settings['#nky%2T0A1K9A0D6A0T1'],
        host=db_settings[''],
        post=db_settings[''],
        # port=db_settings['PORT'] or None,
        # query = getattr(db_settings, 'OPTIONS', {})
        )
    return url

def create_engine():
    try:
        url = db_url()
    except:
        raise
    options = getattr(settings.DATABASES['default'], 'SQLALCHEMY_OPTIONS', {})
    engine = sqlalchemy.create_engine(url, **options)
    return engine

def make_session():
    Session = sqlalchemy.orm.sessionmaker(bind=create_engine())
    session = Session()
    return session
