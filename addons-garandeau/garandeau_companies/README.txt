sudo apt-get install python-dateutil python-feedparser python-ldap python-libxslt1 python-lxml python-mako python-openid python-psycopg2 python-pybabel python-pychart python-pydot python-pyparsing python-reportlab python-simplejson python-tz python-vatnumber python-vobject python-webdav python-werkzeug python-xlwt python-yaml python-zsi python-docutils python-psutil python-mock python-unittest2 python-jinja2 python-pypdf python-decorator python-requests python-passlib python-pil -y



sudo apt-get install libevent-dev
pip install greenlet
pip install gevent
pip install psycopg2

sudo pip install plop
sudo pip install flamegraph

sudo aptitude install python-psycogreen

Options de lancement :
--config /home/jpbigois/odooAddons/odoo.conf --log-level=debug --dev=all --workers=17 --limit-memory-soft=11408506880  --limit-memory-hard=13690208256
--config /home/jpbigois/odooAddons/odoo.conf --log-level=debug --dev=all --workers=17 --limit-memory-soft=11408506880 --limit-memory-hard=13690208256 --limit-time-cpu=240 --limit-time-real=480


/etc/postgresql/9.5/main/postgresql.conf -> postgres.com mettre :
shared_buffers = 3072MB
effective_cache_size = 8192MB