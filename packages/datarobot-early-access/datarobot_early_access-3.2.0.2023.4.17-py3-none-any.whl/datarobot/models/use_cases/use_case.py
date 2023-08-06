#
# Copyright 2023 DataRobot, Inc. and its affiliates.
#
# All rights reserved.
#
# DataRobot, Inc.
#
# This is proprietary source code of DataRobot, Inc. and its
# affiliates.
#
# Released under the terms of DataRobot Tool and Utility Agreement.
from __future__ import annotations

from typing import Dict, List, Optional, Tuple, Union

import trafaret as t

from datarobot.enums import UseCaseEntities
from datarobot.errors import InvalidUsageError
from datarobot.models.api_object import APIObject
from datarobot.models.dataset import Dataset
from datarobot.models.project import Project
from datarobot.utils.pagination import unpaginate

use_case_user_trafaret = t.Dict(
    {
        t.Key("id"): t.String,
        t.Key("full_name", optional=True): t.Or(t.String, t.Null),
        t.Key("email", optional=True): t.Or(t.String, t.Null),
        t.Key("userhash", optional=True): t.Or(t.String, t.Null),
        t.Key("username", optional=True): t.Or(t.String, t.Null),
    }
).ignore_extra("*")


class UseCaseUser(APIObject):
    """Experiment container user.

    Attributes
    ----------
    id : str
        The id of the user.
    full_name : str
        The full name of the user. Optional.
    email : str
        The email address of the user. Optional.
    userhash : str
        User's gravatar hash. Optional.
    username : str
        The username of the user. Optional.
    """

    _converter = use_case_user_trafaret

    def __init__(
        self,
        id: str,
        full_name: Optional[str] = None,
        email: Optional[str] = None,
        userhash: Optional[str] = None,
        username: Optional[str] = None,
    ):
        self.id = id
        self.full_name = full_name
        self.email = email
        self.userhash = userhash
        self.username = username


class UseCaseReferenceEntity(APIObject):
    """
    An entity associated with a Use Case.

    Attributes
    ----------
    entity_type : UseCaseEntities
        The type of the entity.
    use_case_id : str
        The Use Case this entity is associated with.
    id : str
        The ID of the entity.
    created_at : str
        The date and time this entity was linked with the Use Case.
    is_deleted : bool
        Whether or not the linked entity has been deleted.
    created : UseCaseUser
        The user who created the link between this entity and the Use Case.
    """

    _converter = t.Dict(
        {
            t.Key("id"): t.String,
            t.Key("entity_type"): t.String,
            t.Key("entity_id"): t.String,
            t.Key("experiment_container_id") >> "use_case_id": t.String,
            t.Key("created_at"): t.String,
            t.Key("created"): use_case_user_trafaret,
            t.Key("is_deleted"): t.Bool,
        }
    ).ignore_extra("*")

    def __init__(
        self,
        id: str,
        entity_type: UseCaseEntities,
        entity_id: str,
        use_case_id: str,
        created_at: str,
        created: Dict[str, str],
        is_deleted: bool,
    ):
        self.id = id
        self.entity_type = entity_type
        self.entity_id = entity_id
        self.use_case_id = use_case_id
        self.created_at = created_at
        self.created = UseCaseUser(**created)
        self.is_deleted = is_deleted


class UseCase(APIObject):
    """Experiment container.

    Attributes
    ----------
    id : str
        The ID of the Use Case.
    name : str
        The name of the Use Case.
    description : str
        The description of the Use Case. Nullable.
    created_at  : str
        The timestamp generated at record creation.
    created : UseCaseUser
        The user who created the Use Case.
    updated_at : str
        The timestamp generated when the record was last updated.
    updated : UseCaseUser
        The most recent user to update the Use Case.
    models_count : int
        The number of models in a Use Case.
    projects_count : int
        The number of projects in a Use Case.
    datasets_count: int
        The number of datasets in a Use Case.
    notebooks_count: int
        The number of notebooks in a Use Case.
    applications_count: int
        The number of applications in a Use Case.
    owners : List[UseCaseUser]
        The most recent user to update the Use Case.
    members : List[UseCaseUser]
        The most recent user to update the Use Case.
    """

    _path = "experimentContainers/"

    _converter = t.Dict(
        {
            t.Key("id"): t.String,
            t.Key("name"): t.String,
            t.Key("description", optional=True): t.Or(t.String, t.Null),
            t.Key("created_at"): t.String,
            t.Key("created"): use_case_user_trafaret,
            t.Key("updated_at"): t.String,
            t.Key("updated"): use_case_user_trafaret,
            t.Key("models_count"): t.Int,
            t.Key("projects_count"): t.Int,
            t.Key("datasets_count"): t.Int,
            t.Key("notebooks_count"): t.Int,
            t.Key("applications_count"): t.Int,
            t.Key("owners", optional=True): t.List(use_case_user_trafaret),
            t.Key("members"): t.List(use_case_user_trafaret),
        }
    ).ignore_extra("*")

    def __init__(
        self,
        id: str,
        name: str,
        created_at: str,
        created: Dict[str, str],
        updated_at: str,
        updated: Dict[str, str],
        models_count: int,
        projects_count: int,
        datasets_count: int,
        notebooks_count: int,
        applications_count: int,
        members: List[Dict[str, str]],
        description: Optional[str] = None,
        owners: Optional[List[Dict[str, str]]] = None,
    ):
        self.id: str = id
        self.name: str = name
        self.description: Optional[str] = description
        self.created_at: str = created_at
        self.created: UseCaseUser = UseCaseUser(**created)
        self.updated_at: str = updated_at
        self.updated: UseCaseUser = UseCaseUser(**updated)
        self.models_count: int = models_count
        self.projects_count: int = projects_count
        self.datasets_count: int = datasets_count
        self.notebooks_count: int = notebooks_count
        self.applications_count: int = applications_count
        self.members: List[UseCaseUser] = [UseCaseUser(**member) for member in members]
        self.owners: Optional[List[UseCaseUser]] = (
            [UseCaseUser(**owner) for owner in owners] if owners else None
        )

    @classmethod
    def get(cls, use_case_id: str) -> UseCase:
        """
        Gets information about a use case.

        Parameters
        ----------
        use_case_id : str
            The identifier of the Use Case you want to load.

        Returns
        -------
        use_case : UseCase
            The queried Use Case.
        """
        path = f"{cls._path}{use_case_id}/"
        return cls.from_location(path)

    @classmethod
    def list(cls, search_params: Optional[Dict[str, Union[str, int]]] = None) -> List[UseCase]:
        """
        Returns the Use Cases associated with this account.

        Parameters
        ----------
        search_params : dict, optional.
            If not `None`, the returned projects are filtered by lookup.
            Currently, you can query use cases by:

            * ``offset`` - The number of records to skip over. Default 0.
            * ``limit`` - The number of records to return in the range from 1 to 100. Default 100.
            * ``search`` - Only return Use Cases with names that match the given string.
            * ``project_id`` - Only return Use Cases associated with the given project ID.
            * ``application_id`` - Only return Use Cases associated with the given app.
            * ``sort`` - The order to sort the experience containers.

            ``sort`` queries can use the following options:

            * ``id`` or ``-id``
            * ``name`` or ``-name``
            * ``description`` or ``-description``
            * ``projects_count`` or ``-projects_count``
            * ``datasets_count`` or ``-datasets_count``
            * ``notebooks_count`` or ``-notebooks_count``
            * ``applications_count`` or ``-applications_count``
            * ``created_at`` or ``-created_at``
            * ``created_by`` or ``-created_by``
            * ``updated_at`` or ``-updated_at``
            * ``updated_by`` or ``-updated_by``

        Returns
        -------
        use_cases : list of UseCase instances
            Contains a list of Use Cases associated with this user
            account.

        Raises
        ------
        TypeError
            Raised if ``search_params`` parameter is provided,
            but is not of supported type.
        """
        get_params = {}
        if search_params is not None:
            if isinstance(search_params, dict):
                get_params.update(search_params)
            else:
                raise TypeError(
                    "Provided search_params argument {} is invalid type {}".format(
                        search_params, type(search_params)
                    )
                )
        r_data = unpaginate(cls._path, get_params, cls._client)
        return [cls.from_server_data(item) for item in r_data]

    @classmethod
    def create(cls, name: Optional[str] = None, description: Optional[str] = None) -> UseCase:
        """
        Create a new Use Case.

        Parameters
        ----------
        name : str
            Optional. The name of the new Use Case.
        description: str
            The description of the new Use Case. Optional.

        Returns
        -------
        use_case : UseCase
            The queried Use Case.
        """
        payload = {"name": name, "description": description}
        use_case_id = cls._client.post(cls._path, data=payload).json()["id"]
        return cls.get(use_case_id)

    @classmethod
    def delete(cls, use_case_id: str) -> None:
        """
        Delete a Use Case.

        Parameters
        ----------
        use_case_id : str
            The ID of the Use Case to be deleted.
        """
        path = f"{cls._path}{use_case_id}/"
        cls._client.delete(path)
        return None

    def update(self, name: Optional[str] = None, description: Optional[str] = None) -> UseCase:
        """
        Update a Use Case's name or description.

        Parameters
        ----------
        name : str
            The updated name of the Use Case.
        description : str
            The updated description of the Use Case.

        Returns
        -------
        use_case : UseCase
            The updated Use Case.
        """
        payload = {"name": name, "description": description}
        path = f"{self._path}{self.id}/"
        r_data = self._client.patch(path, data=payload).json()
        return self.from_server_data(r_data)

    def _get_reference_entity_info(
        self, entity: Union[UseCaseReferenceEntity, Project, Dataset]
    ) -> Tuple[UseCaseEntities, str]:
        """
        Get the entity type and entity id for a reference entity instance
        Parameters
        ----------
        entity : Union[UseCaseReferenceEntity, Project, Dataset]
            The entity instance to add to a Use Case.
        Returns
        -------
        entity_info : Tuple[UseCaseEntities, str]
            The entity type and entity id
        """
        entity_type = None
        entity_id = None
        if isinstance(entity, Project):
            entity_type = UseCaseEntities.PROJECT
            entity_id = entity.id
        elif isinstance(entity, Dataset):
            entity_type = UseCaseEntities.DATASET
            entity_id = entity.id
        elif isinstance(entity, UseCaseReferenceEntity):
            entity_type = entity.entity_type
            entity_id = entity.entity_id
        return entity_type, entity_id  # type: ignore[return-value]

    def add(
        self,
        entity: Optional[Union[UseCaseReferenceEntity, Project, Dataset]] = None,
        entity_type: Optional[UseCaseEntities] = None,
        entity_id: Optional[str] = None,
    ) -> UseCaseReferenceEntity:
        """
        Add an entity (project, notebook, dataset, etc.) to a Use Case. Can only accept either an entity or
        an entity type and entity ID, but not both.

        Parameters
        ----------
        entity : Union[UseCaseReferenceEntity, Project, Dataset]
            An existing entity linked to a different Use Case to be linked to this Use Case.
            Can not be used if entity_type and entity_id are passed.
        entity_type : UseCaseEntities
            The entity type of the entity to link to this Use Case. Can not be used if entity is passed.
        entity_id : str
            The ID of the entity to link to this Use Case. Can not be used if entity is passed.

        Returns
        -------
        use_case_reference_entity : UseCaseReferenceEntity
            The newly created reference link between this Use Case and the entity.
        """
        e_type = entity_type
        e_id = entity_id
        if entity and (e_type or entity_id):
            raise InvalidUsageError(
                "Can only except either an entity, or an entity type and entity id."
            )
        if not entity and (not e_type or not entity_id):
            raise InvalidUsageError("Missing entity, or an entity type and entity id.")
        if entity:
            e_type, e_id = self._get_reference_entity_info(entity)
        path = f"{self._path}{self.id}/{e_type}/{e_id}/"
        r_data = self._client.post(path)
        return UseCaseReferenceEntity.from_server_data(r_data.json())

    def remove(
        self,
        entity: Optional[Union[UseCaseReferenceEntity, Project, Dataset]] = None,
        entity_type: Optional[UseCaseEntities] = None,
        entity_id: Optional[str] = None,
    ) -> None:
        """
        Remove an entity from a Use Case. Only supports passing an entity instance, or an entity type and ID.

        Parameters
        ----------
        entity : Union[UseCaseReferenceEntity, Project, Dataset]
            An existing entity instance to be removed from a Use Case.
            Can not be used if entity_type and entity_id are passed.
        entity_type : UseCaseEntities
            The entity type of the entity to link to this Use Case. Can not be used if entity is passed.
        entity_id : str
            The ID of the entity to link to this Use Case.  Can not be used if entity is passed.
        """
        e_type = entity_type
        e_id = entity_id
        if entity and (entity_type or entity_id):
            raise InvalidUsageError(
                "Can only except either an entity, or an entity type and entity id."
            )
        if not entity and (not entity_type or not entity_id):
            raise InvalidUsageError("Missing entity, or an entity type and entity id.")
        if entity:
            e_type, e_id = self._get_reference_entity_info(entity)
        path = f"{self._path}{self.id}/{e_type}/{e_id}/"
        self._client.delete(path)
        return None
