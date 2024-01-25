
file = open('openapi.yaml', 'r')
openapi_contents = file.read()
prompt = f"""
You are a helpful assistant tasked to extract act frames from sources of norms.

An act frame describes the normative actions that can
be performed by an actor, if a certain precondition
holds, and when performed has an effect on the agent
bound by the action: the recipient. Act frames con-
tain an action, actor, object, recipient, precondition and
postcondition. The postcondition contains the result of
an action, which can be the creation or termination of
one or more facts or duties. 

The actor, object and recipient are all se-
mantic roles of the action. Note that the reverse is not
true: if we obtain actors, objects and recipients from
a text, they are not necessarily part of an act frame.
As stated before, act frames describe not any action
but specific normative actions that have an effect in the
real world, such as granting an application.



You will now receive another source of a norm. 
Please execute the following steps (and only the following steps):
1. open with three dollar signs ($$$)
2. Provide 5 to 10 lines of reasoning about the norm you received and what components of the act frame you identify.
3. close with three dollar signs ($$$)
4. Open with three backticks (```)
5. Provide the ACT frame in a json that conforms to the following openapi specification:

{openapi_contents}

6. Close with three backticks (```)

"""

