# FLINT-conversation-service

## About
The back-end layer of the Flint-it application prototype.

The back-end layer takes as an input any string (which is expected to correspond to some source of a norm) and returns (1) all the ACT frames it could identify and generate from that string in JSON format and (2) the reasoning steps it used to construct those frames in natural language. 

The backend layer implements three main subcomponents: 

The first subcomponent is responsible for taking the input string and redirecting it to the ChatGPT API as a user prompt. As a system prompt, it uses a locally stored prompt that is experimentally fine-tuned to generate ACT frames for sources of norms. 

The second subcomponent is responsible for splitting the previous response up into  two parts: One part that described the reasoning steps used to generate the ACT frames and one part that describes the generated ACT frames in semi-structured format. 

The third and final subcomponent is responsible for transforming the semi-structured ACT frames into json format and send them back as a response together with the reasoning steps. To transform the ACT frames into JSON format, this subcomponent sends the semi-structured ACT-FRAMES to the ChatGPT API as a user prompt while using a system prompt a locally stored prompt experimentally fine-tuned to transform the semi-structured output from the previous step into json format. This is the component that ultimately ensures the service implements the capabilities described in the OAS as dicussed in section \ref{OAS}.



## Usage

flask --app app run