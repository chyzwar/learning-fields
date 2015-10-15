from client import Client


class StandardClient(Client):

    """StandardClient class inherit from Client"""

    def __init__(self, client_id, call_plan, client_type):
        super(StandardClient, self).__init__(client_id, call_plan)
        self.__client_type = client_type

    def call_cost(self, call):
        """Calcucalte Cost of call"""
        try:
            cost = self.per_minute(call.call_type) * call.call_duration

            if call.is_international:
                rate = self.call_plan.plan_tariffs['international_rate']
                cost = cost * rate

            return cost

        except KeyError, e:
            print 'I got a KeyError - reason "%s"' % str(e)

    def per_minute(self, call_type):
        "Calculate per minute base cost"
        try:
            per_minute = self.call_plan.plan_tariffs[call_type]

            return per_minute

        except KeyError, e:
            print 'I got a KeyError - reason "%s"' % str(e)

    @property
    def client_type(self):
        return self.__client_type

    @client_type.setter
    def call_type(self, value):
        self.__client_type = value
