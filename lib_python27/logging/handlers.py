logger = None
class BaseHandler(object):
    pass


class SampleHandler(BaseHandler):

    def PUT(self, id):
        logger.debug('SampleHandler: PUT request with id %s' % id)
        # ...

    def POST(self, id):
        logger.debug('SampleHandler: POST request with id %s' % id)
        # ...




