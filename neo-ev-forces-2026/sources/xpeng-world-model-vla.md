---
title: "XPENG Releases World Model Technical Report, Powering VLA 2.0 Model R&D and Verification"
site: "xpeng.com"
source: "https://www.xpeng.com/pressroom/news/019dd72da86c9dd703de8a0282290002"
domain: "xpeng.com"
language: "en"
description: "XPENG Releases World Model Technical Report, Powering VLA 2.0 Model R&D and Verification"
word_count: 1225
---

**Guangzhou, April 29, 2026** — XPENG (NYSE: XPEV, HKEX: 9868), a leading China-based high-tech company, recently officially released its X-World Technical Report, providing a comprehensive breakdown of the model's construction and deployment across data, architecture, training, validation, and application. X-World is a controllable, multi-view generative world model designed for autonomous driving. Built on video diffusion technology, it features real-time response and continuous generation capabilities across multiple perspectives.

The report highlights X-World's practical value within XPENG's autonomous driving ecosystem, where it is already integrated into production workflows such as closed-loop simulation, online reinforcement learning, and data synthesis. Furthermore, during the recent rollout of VLA 2.0 to users, X-World has been extensively utilized for environmental simulation and model evaluation throughout the R&D and validation phases.

![](https://s-cdn.xpeng.com/commoncms/prod/2026-04-29/3ff7b14b7a474dc785709dd794140c16.png)

The evaluation of autonomous driving systems primarily relies on real-world road testing and simulation testing. Among these, simulation testing possesses advantages such as lower costs, higher efficiency, broader scenario coverage, and repeatable verification. Traditional simulation evaluation extensively adopts technical roadmaps based on 3D Gaussian Splatting (3DGS). While these methods can reproduce real-world scenes to a certain extent, they often struggle to effectively generate and evaluate subsequent scenes beyond the existing reconstruction range when an autonomous driving model produces behaviors that significantly deviate from the original collected trajectory, such as sharp lane changes or detours. Consequently, the industry still relies heavily on real-vehicle road testing, a method characterized by high costs, limited scenario coverage, and the difficulty of reproducing specific situations.

To resolve these bottlenecks, the XPENG Generative World Model team sought to build a "real-world simulator" capable of generating future videos that comply with physical constraints under given action conditions, while maintaining high controllability and stability throughout the continuous generation process. In this context, X-World was born. By inputting multi-camera historical video streams and the driving actions (or action sequences) to be executed, it can generate corresponding future multi-camera video streams. X-World can be regarded as a physical AI system that "thinks" about driving scenes, capable of imagining changes in road conditions seconds into the future based on current road status and driving operations.

At the architectural level, X-World is built upon the leading video generation model WAN 2.2, following its latent space video generation paradigm by combining a video VAE with a DiT-based latent space denoiser. The underlying layer adopts a high-compression ratio 3D Causal Autoencoder (VAE), which significantly reduces computational and memory overhead and supports long-sequence video modeling, thereby better capturing rich spatio-temporal dependencies while reducing latency and accelerating inference speeds. The model backbone is a customized DiT network that achieves joint modeling of temporal and view dimensions through a view-temporal self-attention mechanism, ensuring consistency across 7-way camera views. X-World also provides a comprehensive set of conditional control interfaces, including ego-vehicle actions, dynamic traffic participants, static road elements (such as lane lines and road boundaries), and camera intrinsics and extrinsics, allowing for fine-grained regulation of the driving scene generation process. Together, these designs achieve controllable multi-view generation under multiple input conditions.

![](https://s-cdn.xpeng.com/commoncms/prod/2026-04-29/6886e19ddbad4b878845cbcb202b0d50.png)

In this technical report, the XPENG team shares the technical challenges encountered during the actual deployment of X-World. The core focus lies in achieving cross-view 3D consistency, accurate multi-condition controlled generation, and long-sequence frame generation. In addition to novel attempts in model architecture, the team adopted a two-stage training approach at the training level:

**\-Phase One:** Transforming a large pre-trained video generation model into a fully controllable multi-camera world model.

**\-Phase Two:** Converting the model into a streaming autoregressive simulator through a "block-causal architecture" and "few-step self-forcing learning," combined with rolling Key-Value (KV) cache.

Unlike traditional bidirectional video diffusion models, X-World operates in a streaming autoregressive manner, allowing it to progressively generate future video frames for real-time interaction. This design makes the model naturally suitable for closed-loop scenarios, providing support for the scalable evaluation of end-to-end policies while also enabling its application in online reinforcement learning training.

**Experimental results show that X-World enables high-quality multi-view video generation. Overall, it offers three core strengths:**
\- **Strong cross-view consistency,** ensuring that geometric information and object characteristics remain aligned across the seven surround-view cameras;
\- **Strict action following**, with generated future scenes closely matching the ego vehicle behavior specified by the instruction;
\- **Long-horizon video simulation capabilities,** enabling stable predictions over extended time spans. Taken together, these capabilities bring generative world models closer to a practical “real-world simulator,” providing VLA-based autonomous driving systems with reproducible benchmark testing, scalable regression testing, and support for interactive learning.

In terms of applications, X-World is more than just a video generation model. It is a high-fidelity, interactive, and controllable underlying foundation platform that supports the development and validation of XPENG’s VLA 2.0. At present, X-World is already playing a supporting role in XPENG’s closed-loop simulation testing, online reinforcement learning, and data generation for autonomous driving.

\- **Built on X-World, XPENG has developed a closed-loop evaluation engine for VLA 2.0.** Unlike traditional approaches based on 3D reconstruction, X-World supports interactive simulation and the evaluation of safety-critical metrics. For example, running VLA 2.0 in X-World makes it possible to assess performance indicators such as collision rate, goal completion progress, and ride comfort in a virtual environment that closely reflects the visual distribution of the real world. At present, XPENG’s autonomous driving simulation scenarios have grown from 30,000 one year ago to more than 500,000, with daily simulated test mileage equivalent to 30 million kilometers of real-world driving.
\- **X-World can serve as a simulation platform for online reinforcement learning.** Leveraging X-World’s controllability, XPENG can focus on optimizing the model for difficult driving scenarios, such as pedestrian “dart-outs” at intersections and hesitation during lane changes in congested traffic.
\- **X-World enables large-scale data generation and augmentation.** As a generative data factory, X-World can generate missing long-tail scenario data to improve VLA 2.0’s ability to handle corner cases, while also generating overseas data for model training, thereby accelerating XPENG’s global autonomous driving deployment.

In addition to the official release of its world model technical report, XPENG has rolled out VLA 2.0 to users this month, delivering a comprehensively enhanced driving experience. From cutting-edge research to real-world engineering deployment, XPENG continues to leverage advanced technologies and strong technical capabilities to provide full-scenario intelligent driving that is safer, more reliable, and more efficient—bringing truly safe and intelligent autonomous driving to every road.

For more information, please refer to the full paper and the official website:
Paper address: [https://arxiv.org/abs/2603.19979](https://arxiv.org/abs/2603.19979)
Website: [https://x-world-1.github.io/](https://x-world-1.github.io/)

\---
**About XPENG
**Founded in 2014, XPENG is a leading Chinese AI-driven mobility company that designs, develops, manufactures, and markets Smart EVs, catering to a growing base of tech-savvy consumers. With the rapid advancement of AI, XPENG aspires to become a global leader in AI mobility, with a mission to drive the Smart EV revolution through cutting-edge technology, shaping the future of mobility.
To enhance the customer experience, XPENG develops its full-stack advanced driver-assistance system (ADAS) technology and intelligent in-car operating system in-house, along with core vehicle systems such as the powertrain and electrical/electronic architecture (EEA). Headquartered in Guangzhou, China, XPENG also operates key offices in Beijing, Shanghai, Silicon Valley, and Amsterdam. Its Smart EVs are primarily manufactured at its facilities in Zhaoqing and Guangzhou, Guangdong province.
XPENG is listed on the New York Stock Exchange (NYSE: XPEV) and Hong Kong Exchange (HKEX: 9868).
For more information, please visit [https://www.xpeng.com/](https://www.xpeng.com/).

**Contacts**:
For Media Enquiries:
XPENG PR Department
Email: pr@xiaopeng.com