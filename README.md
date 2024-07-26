# Health-Situation-in-Morocco

## Table of Contents
- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Difficulties](#difficulties)
- [Points to Improve](#points-to-improve)
- [Tools](#tools)
- [Contributing](#contributing)
- [License](#license)
  
## Overview

The **Health-Situation-in-Morocco** project focuses on analyzing the private healthcare sector in Morocco. This project aims to provide a comprehensive assessment of various health infrastructure indicators across different regions of the country. Key aspects of the analysis include:

- **Number of Clinics per Region**: Evaluating the distribution of private clinics across various regions.
- **Number of Doctors**: Analyzing the availability of doctors in different areas.
- **Affiliates' Declarations**: Examining data related to the declarations made by affiliates, including health insurance claims and coverage details.
- **Number of Pensioned Insured Individuals**: Tracking the count of insured individuals who are currently receiving pensions.
- **Declared Payroll**: Assessing the reported payroll for healthcare employees within the private sector.
- **Population per Primary Healthcare Facility**: Calculating the number of residents served by each basic healthcare facility.
- **Population per Nurse**: Evaluating the ratio of residents to nurses to gauge healthcare accessibility.
- **Evolution of Primary Healthcare Facilities**: Monitoring the growth and changes in primary healthcare establishments over time.

The project aims to offer valuable insights into the private healthcare sector’s capacity, distribution, and resource allocation, facilitating better decision-making and planning for health services improvements.

## Installation

To set up the project locally, follow these steps:

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/Samiha128/Health-Situation-in-Morocco.git
    ```
2. **Navigate to the Project Directory**:

    ```bash
    cd Health-Situation-in-Morocco
    ```

3. **Install Dependencies for Dagster**:

    This project uses Dagster for data orchestration. Ensure you have an account with Azure, SQL Server, and Power BI as these services are required for the project's full functionality.

    - **Install Dagster**:

        ```bash
        pip install dagster dagit  # Install Dagster and Dagit for development
        ```

4. **Configure Azure, SQL Server, and Power BI**:

    - **Azure**: Set up an Azure account and configure your resources according to your project needs. Ensure you have access to necessary Azure services.

    - **SQL Server**: Configure SQL Server and provide the connection details in the project's configuration files.

    - **Power BI**: Set up Power BI and configure it for data visualization as needed by the project.
      
  ## Usage

The **Health-Situation-in-Morocco** project is designed to provide valuable insights into the healthcare sector in Morocco, with comparisons to other countries. Here’s how this project can be useful:

- **Assessment of Healthcare Levels in Morocco**: The project helps understand the state of the healthcare sector in Morocco by providing detailed data on the number of existing hospitals, as well as the growth rate of these facilities over time.

- **Regional Analysis of Doctors**: It allows for examining the distribution of doctors across different regions of Morocco, providing an overview of medical access on a regional scale.

- **International Comparison**: Although the project primarily focuses on Morocco, the collected and analyzed data can be used to compare Morocco’s healthcare situation with that of other countries. This includes comparing hospital infrastructure and medical resources available relative to other regions.

- **Tracking the Evolution of Medical Resources**: The project enables tracking the evolution of the number of hospitals and doctors over time, providing key indicators to assess the improvement or deterioration of healthcare services in the country.

By using this project, policymakers, researchers, and analysts can gain a clearer and more comprehensive view of the healthcare situation in Morocco, as well as useful comparisons with other countries to better understand the strengths and challenges of the Moroccan healthcare system.


