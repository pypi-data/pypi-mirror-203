"""
(c) 2021 Firemon

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

# Standard packages
import datetime
import logging

# Local packages
from firemon_api.apps.securitymanager.siql import Siql
from firemon_api.core.endpoint import Endpoint
from firemon_api.core.response import Record, JsonField
from firemon_api.core.query import Request
from .siql import SiqlPP

log = logging.getLogger(__name__)


class PacketTask(Record):
    """Represents the Packet Task for the Packet/Ticket record"""

    _ep_name = "packet-task"
    _is_domain_url = True

    def __init__(self, config, app, packet_id):
        super().__init__(config, app)
        self._packet_id = packet_id
        self._ep_url = (
            f"{self._domain_url}/workflow/{self._config['workflowTask']['workflowVersion']['id']}/"
            f"task/{self._config['workflowTask']['id']}/packet/{self._packet_id}/{self.__class__._ep_name}"
        )

        self._pp_rec_url = (
            f"{self._app_url}/policyplan/domain/{self._app._app.api.domain_id}/"
            f"workflow/{self._config['workflowTask']['workflowVersion']['id']}"
        )
        self._url = self._url_create()

    def requirement(self, config: dict):
        """Add a requirement

        Args:
            config (dict): Good luck
        """

        key = f"task/{self._config['workflowTask']['id']}/packet/{self._packet_id}/requirement"
        req = Request(
            base=self._pp_rec_url,
            key=key,
            session=self._session,
        )
        return req.post(json=config)

    def assign(self, id: str):
        """Assign a packet task"""
        key = "assign"
        headers = self._session.headers
        headers.update({"Content-Type": "text/plain"})
        req = Request(
            base=self._url,
            key=key,
            headers=headers,
            session=self._session,
        )
        return req.put(data=str(id))

    def unassign(self):
        """Unassign a packet task"""
        key = "unassign"
        headers = self._session.headers
        headers.update({"Content-Type": "text/plain"})
        req = Request(
            base=self._url,
            key=key,
            headers=headers,
            session=self._session,
        )
        return req.put()

    def complete(self):
        """Complete a packet task"""
        key = "complete"
        filters = {"button": "submit"}
        req = Request(
            base=self._url,
            key=key,
            filters=filters,
            session=self._session,
        )
        return req.put()


class PacketTasks(Endpoint):
    """Represents the Packet Task for the Packets/Tickets endpoint

    Args:
        api (obj): FiremonAPI()
        app (obj): App()
        packet_id (int): Packet Id

    Kwargs:
        record (obj): default `Record` object
    """

    ep_name = "packet-tasks"
    _is_domain_url = True

    def __init__(self, api, app, packet_id, record=PacketTask):
        self.return_obj = record
        self.api = api
        self.session = api.session
        self.app = app
        self.base_url = api.base_url
        self.app_url = app._app_url
        self.domain_url = app._domain_url
        self.url = None
        if self.__class__._is_domain_url and self.__class__.ep_name:
            self.url = f"{self.domain_url}/{self.__class__.ep_name}"
        elif self.__class__.ep_name:
            self.url = f"{self.app_url}/{self.__class__.ep_name}"

        # These will be used update `key` values for `query.Request`
        # (i.e. they will be appended to 'self.url' to get full path)
        # All child classes can then update to append endpoint actions
        # or add new actions, hopefully for read-ability
        self._ep = {
            "all": None,
            "filter": None,
            "create": None,
            "count": None,
        }
        self._packet_id = packet_id

    def _response_loader(self, values, packet_id):
        return self.return_obj(values, self.app, packet_id)

    def all(self):
        p_tasks = []
        for wfpt in sorted(
            self.app._config["workflowPacketTasks"], key=lambda p: p["id"]
        ):
            p_tasks.append(self._response_loader(wfpt, self._packet_id))
        return p_tasks

    def get(self, *args, **kwargs):
        """Query and retrieve individual PacketTask

        Args:
            *args: packet task id
            **kwargs: key value pairs in a device pack dictionary

        Return:
            PacketTask(object): a PacketTask(object)

        Examples:

        >>>
        """

        pt_all = self.all()
        try:
            # Only getting exact matches
            id = args[0]
            pt_l = [pt for pt in pt_all if pt.id == id]
            if len(pt_l) == 1:
                return pt_l[0]
            else:
                raise Exception(f"The requested Packet Task: {id} could not be found")
        except IndexError:
            id = None

        if not id:
            filter_lookup = self.filter(**kwargs)
            if filter_lookup:
                if len(filter_lookup) > 1:
                    raise ValueError(
                        "get() returned more than one result."
                        "Check the kwarg(s) passed are valid or"
                        "use filter() or all() instead."
                    )
                else:
                    return filter_lookup[0]
            return None

    def filter(self, **kwargs):
        """Retrieve a filterd list of PacketTasks

        Args:
            **kwargs: key value pairs in a device pack dictionary

        Return:
            list: a list of PacketTask(object)

        Examples:

        >>>
        """

        pt_all = self.all()
        if not kwargs:
            raise ValueError("filter must have kwargs")

        return [pt for pt in pt_all if kwargs.items() <= dict(pt).items()]

    def last_modified(self):
        """Get task by last modified date"""
        return sorted(
            self.all(),
            key=lambda p: datetime.datetime.fromisoformat(
                p.lastModifiedDate.rstrip("Z")
            ),
        )[-1]


class Packet(Record):
    """Represents the Packet/Ticket record"""

    _ep_name = "packet"
    _is_domain_url = True

    def __init__(self, config, app):
        super().__init__(config, app)

        if self.__class__._is_domain_url and self.__class__._ep_name:
            self._ep_url = f"{self._domain_url}/workflow/{self._config['workflowVersion']['id']}/{self.__class__._ep_name}"
        self._url = self._url_create()

        self.pt = PacketTasks(self._app.api, self, self.id)

    def save(self):
        """Someday... maybe"""
        raise NotImplementedError("Writes are not supported for this Record.")

    def update(self):
        """Someday... maybe"""
        raise NotImplementedError("Writes are not supported for this Record.")

    def delete(self):
        raise NotImplementedError("Writes are not supported for this Record.")


class Packets(Endpoint):
    """Represents the Packets/Tickets endpoint

    Args:
        api (obj): FiremonAPI()
        app (obj): App()

    Kwargs:
        record (obj): default `Record` object
    """

    ep_name = "packet"
    _is_domain_url = True

    def __init__(self, api, app, wf_id, record=Packet):
        super().__init__(api, app, record=Packet)
        self._wf_id = wf_id

        if self.__class__._is_domain_url and self.__class__.ep_name:
            self.url = (
                f"{self.domain_url}/workflow/{self._wf_id}/{self.__class__.ep_name}"
            )

    def all(self):
        siql_ep = SiqlPP(self.api, self.app)
        siql = f"ticket{{workflow={self._wf_id}}}"
        tickets = siql_ep.ticket(siql)
        return [self.get(ticket.id) for ticket in tickets]

    def get(self, *args, **kwargs):
        try:
            id = str(args[0])
        except IndexError:
            id = None

        if not id:
            if kwargs:
                filter_lookup = self.filter(**kwargs)
            else:
                filter_lookup = self.filter(*args)
            if filter_lookup:
                if len(filter_lookup) > 1:
                    raise ValueError(
                        "get() returned more than one result. "
                        "Check that the kwarg(s) passed are valid for this "
                        "endpoint or use filter() or all() instead."
                    )
                else:
                    return filter_lookup[0]
            return None

        key = f"{id}"

        req = Request(
            base=self.url,
            key=key,
            session=self.session,
        )

        return self._response_loader(req.get())

    def filter(self, *args, **kwargs):
        """Attempt to use the filter options. Really only a single query

        Kwargs:
            siql (str): whatever siql query for tickets is available
        """

        if args:
            kwargs.update({"siql": args[0]})

        if not kwargs:
            raise ValueError("filter must be passed kwargs. Perhaps use all() instead.")

        siql_ep = SiqlPP(self.api, self.app)
        siql = f"ticket{{{kwargs['siql']}}}"
        tickets = siql_ep.ticket(siql)
        return [self.get(ticket.id) for ticket in tickets]

    def create(self, config: dict = None):
        """Create a workflow packet/ticket instance

        Kwargs:
            config (dict):
        """

        if not config:
            config = {}

        resp = Request(
            base=self.url,
            session=self.session,
        ).post(json=config)

        return self._response_loader(resp)
