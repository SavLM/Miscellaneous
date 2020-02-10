# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page
from twilio.rest.insights.v1.call.event import EventList
from twilio.rest.insights.v1.call.metric import MetricList
from twilio.rest.insights.v1.call.summary import CallSummaryList


class CallList(ListResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version):
        """
        Initialize the CallList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.insights.v1.call.CallList
        :rtype: twilio.rest.insights.v1.call.CallList
        """
        super(CallList, self).__init__(version)

        # Path Solution
        self._solution = {}

    def get(self, sid):
        """
        Constructs a CallContext

        :param sid: The sid

        :returns: twilio.rest.insights.v1.call.CallContext
        :rtype: twilio.rest.insights.v1.call.CallContext
        """
        return CallContext(self._version, sid=sid, )

    def __call__(self, sid):
        """
        Constructs a CallContext

        :param sid: The sid

        :returns: twilio.rest.insights.v1.call.CallContext
        :rtype: twilio.rest.insights.v1.call.CallContext
        """
        return CallContext(self._version, sid=sid, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Insights.V1.CallList>'


class CallPage(Page):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, response, solution):
        """
        Initialize the CallPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.insights.v1.call.CallPage
        :rtype: twilio.rest.insights.v1.call.CallPage
        """
        super(CallPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of CallInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.insights.v1.call.CallInstance
        :rtype: twilio.rest.insights.v1.call.CallInstance
        """
        return CallInstance(self._version, payload, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Insights.V1.CallPage>'


class CallContext(InstanceContext):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, sid):
        """
        Initialize the CallContext

        :param Version version: Version that contains the resource
        :param sid: The sid

        :returns: twilio.rest.insights.v1.call.CallContext
        :rtype: twilio.rest.insights.v1.call.CallContext
        """
        super(CallContext, self).__init__(version)

        # Path Solution
        self._solution = {'sid': sid, }
        self._uri = '/Voice/{sid}'.format(**self._solution)

        # Dependents
        self._events = None
        self._metrics = None
        self._summary = None

    def fetch(self):
        """
        Fetch the CallInstance

        :returns: The fetched CallInstance
        :rtype: twilio.rest.insights.v1.call.CallInstance
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return CallInstance(self._version, payload, sid=self._solution['sid'], )

    @property
    def events(self):
        """
        Access the events

        :returns: twilio.rest.insights.v1.call.event.EventList
        :rtype: twilio.rest.insights.v1.call.event.EventList
        """
        if self._events is None:
            self._events = EventList(self._version, call_sid=self._solution['sid'], )
        return self._events

    @property
    def metrics(self):
        """
        Access the metrics

        :returns: twilio.rest.insights.v1.call.metric.MetricList
        :rtype: twilio.rest.insights.v1.call.metric.MetricList
        """
        if self._metrics is None:
            self._metrics = MetricList(self._version, call_sid=self._solution['sid'], )
        return self._metrics

    @property
    def summary(self):
        """
        Access the summary

        :returns: twilio.rest.insights.v1.call.summary.CallSummaryList
        :rtype: twilio.rest.insights.v1.call.summary.CallSummaryList
        """
        if self._summary is None:
            self._summary = CallSummaryList(self._version, call_sid=self._solution['sid'], )
        return self._summary

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Insights.V1.CallContext {}>'.format(context)


class CallInstance(InstanceResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, payload, sid=None):
        """
        Initialize the CallInstance

        :returns: twilio.rest.insights.v1.call.CallInstance
        :rtype: twilio.rest.insights.v1.call.CallInstance
        """
        super(CallInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload.get('sid'),
            'url': payload.get('url'),
            'links': payload.get('links'),
        }

        # Context
        self._context = None
        self._solution = {'sid': sid or self._properties['sid'], }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: CallContext for this CallInstance
        :rtype: twilio.rest.insights.v1.call.CallContext
        """
        if self._context is None:
            self._context = CallContext(self._version, sid=self._solution['sid'], )
        return self._context

    @property
    def sid(self):
        """
        :returns: The sid
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def url(self):
        """
        :returns: The url
        :rtype: unicode
        """
        return self._properties['url']

    @property
    def links(self):
        """
        :returns: The links
        :rtype: unicode
        """
        return self._properties['links']

    def fetch(self):
        """
        Fetch the CallInstance

        :returns: The fetched CallInstance
        :rtype: twilio.rest.insights.v1.call.CallInstance
        """
        return self._proxy.fetch()

    @property
    def events(self):
        """
        Access the events

        :returns: twilio.rest.insights.v1.call.event.EventList
        :rtype: twilio.rest.insights.v1.call.event.EventList
        """
        return self._proxy.events

    @property
    def metrics(self):
        """
        Access the metrics

        :returns: twilio.rest.insights.v1.call.metric.MetricList
        :rtype: twilio.rest.insights.v1.call.metric.MetricList
        """
        return self._proxy.metrics

    @property
    def summary(self):
        """
        Access the summary

        :returns: twilio.rest.insights.v1.call.summary.CallSummaryList
        :rtype: twilio.rest.insights.v1.call.summary.CallSummaryList
        """
        return self._proxy.summary

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Insights.V1.CallInstance {}>'.format(context)
