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

