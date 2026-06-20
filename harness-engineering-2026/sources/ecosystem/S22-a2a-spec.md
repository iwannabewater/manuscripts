---
source_url: https://a2a-protocol.org/latest/specification/
fetched_for: learn/canonical-article
source_check_date: 2026-06-20
---

[fetch] tier=local status=ok extractor=stdlib hint="install readability-lxml + html2text for cleaner output"
# Overview - A2A Protocol

> Source: https://a2a-protocol.org/latest/specification/

Skip to content

Agent2Agent (A2A) Protocol Specification¶

Latest Released Version 1.0.0

Previous Versions

0.3.0

0.2.6

0.1.0

See Release Notes for changes made between versions.

1. Introduction¶

The Agent2Agent (A2A) Protocol is an open standard designed to facilitate communication and interoperability between independent, potentially opaque AI agent systems. In an ecosystem where agents might be built using different frameworks, languages, or by different vendors, A2A provides a common language and interaction model.

This document provides the detailed technical specification for the A2A protocol. Its primary goal is to enable agents to:

Discover each other's capabilities.

Negotiate interaction modalities (text, files, structured data).

Manage collaborative tasks.

Securely exchange information to achieve user goals without needing access to each other's internal state, memory, or tools.

1.1. Key Goals of A2A¶

Interoperability: Bridge the communication gap between disparate agentic systems.

Collaboration: Enable agents to delegate tasks, exchange context, and work together on complex user requests.

Discovery: Allow agents to dynamically find and understand the capabilities of other agents.

Flexibility: Support various interaction modes including synchronous request/response, streaming for real-time updates, and asynchronous push notifications for long-running tasks.

Security: Facilitate secure communication patterns suitable for enterprise environments, relying on standard web security practices.

Asynchronicity: Natively support long-running tasks and interactions that may involve human-in-the-loop scenarios.

1.2. Guiding Principles¶

Simple: Reuse existing, well-understood standards (HTTP, JSON-RPC 2.0, Server-Sent Events).

Enterprise Ready: Address authentication, authorization, security, privacy, tracing, and monitoring by aligning with established enterprise practices.

Async First: Designed for (potentially very) long-running tasks and human-in-the-loop interactions.

Modality Agnostic: Support exchange of diverse content types including text, audio/video (via file references), structured data/forms, and potentially embedded UI components (e.g., iframes referenced in parts).

Opaque Execution: Agents collaborate based on declared capabilities and exchanged information, without needing to share their internal thoughts, plans, or tool implementations.

For a broader understanding of A2A's purpose and benefits, see What is A2A?.

1.3. Specification Structure¶

This specification is organized into three distinct layers that work together to provide a complete protocol definition:

graph TB
subgraph L1 ["A2A Data Model"]
direction LR
A[Task] ~~~ B[Message] ~~~ C[AgentCard] ~~~ D[Part] ~~~ E[Artifact] ~~~ F[Extension]
end

subgraph L2 ["A2A Operations"]
direction LR
G[Send Message] ~~~ H[Send Streaming Message] ~~~ I[Get Task] ~~~ J[List Tasks] ~~~ K[Cancel Task] ~~~ L[Get Agent Card]
end

subgraph L3 ["Protocol Bindings"]
direction LR
M[JSON-RPC Methods] ~~~ N[gRPC RPCs] ~~~ O[HTTP/REST Endpoints] ~~~ P[Custom Bindings]
end

%% Dependencies between layers
L1 --> L2
L2 --> L3

style A fill:#e1f5fe
style B fill:#e1f5fe
style C fill:#e1f5fe
style D fill:#e1f5fe
style E fill:#e1f5fe
style F fill:#e1f5fe

style G fill:#f3e5f5
style H fill:#f3e5f5
style I fill:#f3e5f5
style J fill:#f3e5f5
style K fill:#f3e5f5
style L fill:#f3e5f5

style M fill:#e8f5e8
style N fill:#e8f5e8
style O fill:#e8f5e8

style L1 fill:#f0f8ff,stroke:#333,stroke-width:2px
style L2 fill:#faf0ff,stroke:#333,stroke-width:2px
style L3 fill:#f0fff0,stroke:#333,stroke-width:2px

Layer 1: Canonical Data Model defines the core data structures and message formats that all A2A implementations must understand. These are protocol agnostic definitions expressed as Protocol Buffer messages.

Layer 2: Abstract Operations describes the fundamental capabilities and behaviors that A2A agents must support, independent of how they are exposed over specific protocols.

Layer 3: Protocol Bindings provides concrete mappings of the abstract operations and data structures to specific protocol bindings (JSON-RPC, gRPC, HTTP/REST), including method names, endpoint patterns, and protocol-specific behaviors.

This layered approach ensures that:

Core semantics remain consistent across all protocol bindings

New protocol bindings can be added without changing the fundamental data model

Developers can reason about A2A operations independently of binding concerns

Interoperability is maintained through shared understanding of the canonical data model

1.4 Normative Content¶

In addition to the protocol requirements defined in this document, the file spec/a2a.proto is the single authoritative normative definition of all protocol data objects and request/response messages. A generated JSON artifact (spec/a2a.json, produced at build time and not committed) MAY be published for convenience to tooling and the website, but it is a non-normative build artifact. SDK language bindings, schemas, and any other derived forms MUST be regenerated from the proto (directly or via code generation) rather than edited manually.

Change Control and Deprecation Lifecycle:

Introduction: When a proto message or field is renamed, the new name is added while existing published names remain available, but marked deprecated, until the next major release.

Documentation: Migration guidance MUST be provided via an ancillary document when introducing major breaking changes.

Anchors: Legacy documentation anchors MUST be preserved (as hidden HTML anchors) to avoid breaking inbound links.

SDK/Schema Aliases: SDKs and JSON Schemas SHOULD provide deprecated alias types/definitions to maintain backward compatibility.

Removal: A deprecated name SHOULD NOT be removed earlier than the next major version after introduction of its replacement.

Automated Generation:

The documentation build generates specification/json/a2a.json on-the-fly (the file is not tracked in source control). Future improvements may publish an OpenAPI v3 + JSON Schema bundle for enhanced tooling.

Rationale:

Centering the proto file as the normative source ensures protocol neutrality, reduces specification drift, and provides a deterministic evolution path for the ecosystem.

2. Terminology¶

2.1. Requirements Language¶

The keywords "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in RFC 2119.

2.2. Core Concepts¶

A2A revolves around several key concepts. For detailed explanations, please refer to the Key Concepts guide.

A2A Client: An application or agent that initiates requests to an A2A Server on behalf of a user or another system.

A2A Server (Remote Agent): An agent or agentic system that exposes an A2A-compliant endpoint, processing tasks and providing responses.

Agent Card: A JSON metadata document published by an A2A Server, describing its identity, capabilities, skills, service endpoint, and authentication requirements.

Message: A communication turn between a client and a remote agent, having a role ("user" or "agent") and containing one or more Parts.

Task: The fundamental unit of work managed by A2A, identified by a unique ID. Tasks are stateful and progress through a defined lifecycle.

Part: The smallest unit of content within a Message or Artifact. Parts can contain text, file references, or structured data.

Artifact: An output (e.g., a document, image, structured data) generated by the agent as a result of a task, composed of Parts.

Streaming: Real-time, incremental updates for tasks (status changes, artifact chunks) delivered via protocol-specific streaming mechanisms.

Push Notifications: Asynchronous task updates delivered via server-initiated HTTP POST requests to a client-provided webhook URL, for long-running or disconnected scenarios.

Context: An optional identifier to logically group related tasks and messages.

Extension: A mechanism for agents to provide additional functionality or data beyond the core A2A specification.

3. A2A Protocol Operations¶

This section describes the core operations of the A2A protocol in a binding-independent manner. These operations define the fundamental capabilities that all A2A implementations must support, regardless of the underlying binding mechanism.

3.1. Core Operations¶

The following operations define the fundamental capabilities that all A2A implementations must support, independent of the specific protocol binding used. For a quick reference mapping of these operations to protocol-specific method names and endpoints, see Section 5.3 (Method Mapping Reference). For detailed protocol-specific implementation details, see:

Section 9: JSON-RPC Protocol Binding

Section 10: gRPC Protocol Binding

Section 11: HTTP+JSON/REST Protocol Binding

3.1.1. Send Message¶

The primary operation for initiating agent interactions. Clients send a message to an agent and receive either a task that tracks the processing or a direct response message.

Inputs:

SendMessageRequest: Request object containing the message, configuration, and metadata

Outputs:

Task: A task object representing the processing of the message, OR

Message: A direct response message (for simple interactions that don't require task tracking)

Errors:

ContentTypeNotSupportedError: A Media Type provided in the request's message parts is not supported by the agent.

UnsupportedOperationError: Messages sent to Tasks that are in a terminal state (TASK_STATE_COMPLETED, TASK_STATE_FAILED, TASK_STATE_CANCELED, TASK_STATE_REJECTED) cannot accept further messages.

TaskNotFoundError: The task ID does not exist or is not accessible.

Behavior:

The agent MAY create a new Task to process the provided message asynchronously or MAY return a direct Message response for simple interactions. The operation MUST return immediately with either task information or response message. Task processing MAY continue asynchronously after the response when a Task is returned.

3.1.2. Send Streaming Message¶

Similar to Send Message but with real-time streaming of updates during processing.

Inputs:

SendMessageRequest: Request object containing the message, configuration, and metadata

Outputs:

Stream Response object containing:

Initial response: Task object OR Message object

Subsequent events following a Task MAY include stream of TaskStatusUpdateEvent and TaskArtifactUpdateEvent objects

Final completion indicator

Errors:

UnsupportedOperationError: Streaming is not supported by the agent (see Capability Validation).

UnsupportedOperationError: Messages sent to Tasks that are in a terminal state (TASK_STATE_COMPLETED, TASK_STATE_FAILED, TASK_STATE_CANCELED, TASK_STATE_REJECTED) cannot accept further messages.

ContentTypeNotSupportedError: A Media Type provided in the request's message parts is not supported by the agent.

TaskNotFoundError: The task ID does not exist or is not accessible.

Behavior:

The operation MUST establish a streaming connection for real-time updates. The stream MUST follow one of these patterns:

Message-only stream: If the agent returns a Message, the stream MUST contain exactly one Message object and then close immediately. No task tracking or updates are provided.

Task lifecycle stream: If the agent returns a Task, the stream MUST begin with the Task object, followed by zero or more TaskStatusUpdateEvent or TaskArtifactUpdateEvent objects. The stream MUST close when the task reaches a terminal state (TASK_STATE_COMPLETED, TASK_STATE_FAILED, TASK_STATE_CANCELED, TASK_STATE_REJECTED).

The agent MAY return a Task for complex processing with status/artifact updates or MAY return a Message for direct streaming responses without task overhead. The implementation MUST provide immediate feedback on progress and intermediate results.

3.1.3. Get Task¶

Retrieves the current state (including status, artifacts, and optionally history) of a previously initiated task. This is typically used for polling the status of a task initiated with Send Message, or for fetching the final state of a task after being notified via a push notification or after a stream has ended.

Inputs:

Represents a request for the GetTask method.

Field
Type
Required
Description

tenant
string
No
Optional. Opaque routing identifier. Must match the tenant value from the selected AgentInterface in the Agent Card when that field is set.

id
string
Yes
The resource ID of the task to retrieve.

historyLength
integer
No
The maximum number of most recent messages from the task's history to retrieve. An unset value means the client does not impose any limit. A value of zero is a request to not include any messages. The server MUST NOT return more messages than the provided value, but MAY apply a lower limit.

See History Length Semantics for details about historyLength.

Outputs:

Task: Current state and artifacts of the requested task

Errors:

TaskNotFoundError: The task ID does not exist or is not accessible.

3.1.4. List Tasks¶

Retrieves a list of tasks with optional filtering and pagination capabilities. This method allows clients to discover and manage multiple tasks across different contexts or with specific status criteria.

Inputs:

Parameters for listing tasks with optional filtering criteria.

Field
Type
Required
Description

tenant
string
No
Optional. Opaque routing identifier. Must match the tenant value from the selected AgentInterface in the Agent Card when that field is set.

contextId
string
No
Filter tasks by context ID to get tasks from a specific conversation or session.

status
