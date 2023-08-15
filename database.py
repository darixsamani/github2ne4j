from typing import ClassVar
import pandas as pd
from neontology import BaseNode, BaseRelationship, init_neontology, auto_constrain


class Repository(BaseNode):

    __primarylabel__: ClassVar[str] = "Repository"
    __primaryproperty__: ClassVar[str] = "url"

    url : str




class Issue(BaseNode):

    __primarylabel__: ClassVar[str] = "Issue"
    __primaryproperty__: ClassVar[str] = "url"

    url : str
    content: str



class PullRequest(BaseNode):

    __primarylabel__: ClassVar[str] = "PullRequest"
    __primaryproperty__: ClassVar[str] = "url"
    url : str
    content: str

class HaveIsuue(BaseRelationship):
    __relationshiptype__: ClassVar[str] = "HAVE_ISSUE"
    
    source: Repository
    target: Issue


class HavePullRequest(BaseRelationship):
    __relationshiptype__: ClassVar[str] = "HAVE_PULL_REQUEST"
    
    source: Repository
    target: PullRequest
