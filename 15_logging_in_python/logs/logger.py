import logging

# configuring logging - basic configuration can only be done once so to see the new effects 
# we need to restart kernel and directly run this cell
logging.basicConfig(
    filename='app.log',
    filemode='w',
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    level=logging.DEBUG,
    datefmt='%Y-%m-%d %H:%M:%S'
)