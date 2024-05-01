<!-- # Linhao-Jasmine-Project-OIM3640 -->

# Project ReadMe - MBTI and Astrological Sign-Based Student Pairing System

Team members: Linhao Jiang, Jasmine Zhang

## Big Idea:

We want to develop a team web platform that aims to improve the group project experience in educational settings. Leveraging the power of OpenAI, specifically ChatGPT, our application will automate the team formation process based on users' astrological signs and MBTI assessments. This innovative approach facilitates the creation of balanced and cohesive teams, where each member's strengths and preferences are optimally aligned for collective success. The platform will support different group sizes, allowing teams from 2 to 4 members, and providing flexibility for different project needs and classroom settings.

## Minimum Viable Product (MVP):

- A code for users to scan and match with their assigned course.
- A simple, intuitive interface for users to input their astrological signs and MBTI.
- An algorithm leveraging ChatGPT to suggest team compositions based on the entered data.
- Support for generating teams of various sizes (2 to 4 members), tailored to the requirements of different classroom projects.

## Learning Goals

### Shared Learning Goals:

1. To master the process of integrating ChatGPT and other APIs into a web application, focusing on seamless data flow and user experience.
2. To enhance our skills in creating a responsive and interactive application
3. To develop the ability to manage projects from concept to development. Including planning, experiments, and revision based on Professor Li's feedback.

### Individual Goal:

1. Jasmine: Learn how to effectively utilize the OpenAI API within a Flask application. And enhance my skills in HTML, aiming to create an accessible and user-friendly web page.
2. Linhao: Apply concepts learned in lectures to real-world cases like this. Furthermore, the ability to make a coherent webpage that combines the use of API and self-design algorithm. 

## Implementation Plan:

- **Front-end**: We plan to use Flask to ensure user experience and development efficiency.
- **Database**: We will need some kind of database/ data management system to store user data.

### Development Phases:

1. **Initial Setup and Research** :We set out to gather all the clues we could about how to best blend personality traits (using the MBTI system) and astrological signs to help students find their perfect project teammates. We stored MBTI and Astrological scores in dictionaries to predefine compatibility scores between different MBTI types and astrological signs. The scores were generated from ChatGpt
2. **Prototype Development**: 
3. **Core Functionality Implementation** : Some core functions include calculate_compatibility(): to calculate the compatibility scores between the user and each group member based on MBTI and astrological sign. It averages the scores from both system and calculate an overall group compatibility score.
clean_text(): were used because during our testing process, we realized that there were some unexpected characters occuring in our analysis. Chatpgt asisted us to remove non-ASCII characters from text. To ensure the text displays clean characters. 
get_compatibiloty_analysis(): is for generating detailed compatility explanations using OpenAi's API. It sends a prompt to the API and processs the response, and then structure it into a format suitable for display. 
4. **Integration and Testing**: I faced issues with incomplete or cut-off responses from the OpenAi API due to the 'max_tokens' parameter beign set too low. Another issues was the unwanted characters or non-English responses. So implemented a 'clean_text' function to sanitize the API outputs. 
5. **Finalization and Documentation**

### Continuous Learning and Adaptation

Given the innovative nature of our project, we anticipate the need for continuous learning, especially in the areas of compatibility algorithms and user experience design. We will allocate time for research and adaptation, ensuring our solution is both effective and user-friendly.

### User Interaction with Webpage

User interaction with the webpage is designed to be intuitive and engaging, ensuring a seamless experience from start to finish. Users are greeted by a straightforward interface prompting them to enter their MBTI personality type and astrological sign through simple dropdown menus when visiting the webpage. Clear instructions and tooltips guide the user through the process, enhancing usability. After submitting their information, users are presented with a report that outlines their compatibility with other students in their class, including detailed explanations of the compatibility metrics used.

## Project Timeline

### Week 1:

- Start drafting project proposal and schedule
- Set up project repository
- start research on ChatGpt integration and web framework capabilities

### Week 2:

- Begin front-end development (UI components).
- Start back-end setup (database).

### Week 3:

- Integrate front-end and back-end.
- Implement the compatibility algorithm.
- Begin internal testing and debugging.

### Week 4:

- Conduct extensive testing, including user acceptance testing.
- Make necessary adjustments based on feedback.
- Prepare for project presentation and submission.

## Collaboration Plan:

We plan to meet weekly to discuss our progress, address any challenges, and plan task distribution. We will use Visual Studio Code Live Share during our coding sessions, to enable both of us to edit and debug code simultaneously.

For day-to-day communication, we will use WeChat for messaging and Slack channels for asking coding-related questions. We aim to keep our conversation straightforward and effective.

For the distribution of the work, we ensure that tasks are aligned with each person's strengths and learning goals. Linhao and Jasmine help each other by being motivated and productive throughout the process, we all hope to deliver a successful project outcome!

## Risks and Limitations

The most significant risk is the complexity of accurately mapping MBTI and astrological compatibility into a coherent and user-friendly system. Addressing this will require careful research and potentially consulting with psychology and astrology experts.

## Additional Course Content

- Advanced Flask features and best practices to optimize web application performance and scalability.
- Comprehensive API integration techniques to enhance the application's functionality and user experience.
- UX/UI design principles to ensure the application is not only functional but also engaging and straightforward for users.
