.. meta::
   :title: Documentation - Acord [Models]
   :type: website
   :url: https://acord.readthedocs.io/api/models.html
   :description: All the models created to simplify interactions with the discord API
   :theme-color: #f54646

.. currentmodule:: acord

******
Models
******
Our models use the ``Pydantic`` module for simple data parsing. 
All methods from :class:`~pydantic.BaseModel` are inherited along with ours.
These methods will not be shown in our docs, you can find them in the ``Pydantic`` documentation.

Snowflake
~~~~~~~~~~
A snowflake is a representation of a discord ID, which is a unique integer.
When working with a class type hinted with :class:`Snowflake`,
its exactly the same as working with a :class:`int`.

Emoji
~~~~~

.. attributetable:: Emoji

.. autoclass:: Emoji
   :members:

Guild
~~~~~

.. attributetable:: Guild

.. autoclass:: Guild
   :members:

Guild Template
~~~~~~~~~~~~~~~

.. attributetable:: GuildTemplate

.. autoclass:: GuildTemplate
   :members:

Invite
~~~~~~

.. attributetable:: Invite

.. autoclass:: Invite
   :members:

Member
~~~~~~

.. attributetable:: Member

.. autoclass:: Member
   :members:

Message
~~~~~~~

.. attributetable:: Message

.. autoclass:: Message
   :members:

Message Reference
~~~~~~~~~~~~~~~~~

.. attributetable:: MessageReference

.. autoclass:: MessageReference
   :members:

Sticker
~~~~~~~

.. attributetable:: Sticker

.. autoclass:: Sticker
   :members:

Stage Channel
~~~~~~~~~~~~~

.. attributetable:: Stage

.. autoclass:: Stage
   :members:

Text Channel
~~~~~~~~~~~~

.. attributetable:: TextChannel

.. autoclass:: TextChannel
   :members:
   :inherited-members:
   :exclude-members: json, dict, construct, update_forward_refs, copy

Thread
~~~~~~

.. attributetable:: Thread

.. autoclass:: Thread
   :members:
   :inherited-members:
   :exclude-members: json, dict, construct, update_forward_refs, copy

Thread Member
~~~~~~~~~~~~~

.. attributetable:: ThreadMember

.. autoclass:: ThreadMember
   :members:

Thread Metadata
~~~~~~~~~~~~~~~

.. attributetable:: ThreadMeta

.. autoclass:: ThreadMeta
   :members:

Role
~~~~

.. attributetable:: Role

.. autoclass:: Role
   :members:

User
~~~~

.. attributetable:: User

.. autoclass:: User
   :members:

Interaction
~~~~~~~~~~~

.. attributetable:: Interaction

.. autoclass:: Interaction
   :members:

Attachment
~~~~~~~~~~

.. attributetable:: Attachment

.. autoclass:: Attachment
   :members:

Category Channel
~~~~~~~~~~~~~~~~

.. attributetable:: CategoryChannel

.. autoclass:: CategoryChannel
   :members:

DM Channels
~~~~~~~~~~~

DM Channel
==========
Between 1 user.

.. attributetable:: DMChannel

.. autoclass:: DMChannel
   :members:

Group DM Channel
================
Between multiple users

.. attributetable:: GroupDMChannel

.. autoclass:: GroupDMChannel
   :members:

Integration
~~~~~~~~~~~

.. attributetable:: Integration

.. autoclass:: Integration
   :members:

Voice Channel
~~~~~~~~~~~~~

.. attributetable:: VoiceChannel

.. autoclass:: VoiceChannel
   :members:

Webhook
~~~~~~~

.. attributetable:: Webhook

.. autoclass:: Webhook
   :members:
