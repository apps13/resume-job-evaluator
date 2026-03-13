from models.evaluation_request import EvaluationRequest

# Dictionary of jobs
JOB_DESCRIPTIONS = [
    {
        "job_id": "backend_engineer_001",
        "job_description": (
            "Looking for a backend engineer with strong Python skills, REST API "
            "design, SQL expertise, and hands-on cloud deployment experience. The "
            "role includes building and maintaining scalable microservices, improving "
            "system reliability and performance, implementing CI/CD pipelines, and "
            "working with Docker and Kubernetes in production environments. Candidates "
            "should be comfortable with PostgreSQL schema design, Redis caching "
            "patterns, monitoring and alerting, and incident response practices. "
            "Experience collaborating with cross-functional teams, writing clear "
            "technical documentation, and mentoring junior engineers is highly "
            "preferred."
        ),
    },
    {
        "job_id": "platform_engineer_001",
        "job_description": (
            "We are hiring a Platform Engineer to improve developer productivity and "
            "system reliability across our cloud-native platform. This role focuses on "
            "building and operating Kubernetes-based infrastructure, standardizing "
            "service deployment patterns, and driving operational excellence through "
            "monitoring, alerting, and incident response best practices. You will work "
            "closely with application teams to improve API reliability, define SLOs, "
            "and automate release workflows using CI/CD tooling. Strong experience with "
            "Docker image design, infrastructure-as-code, cloud networking fundamentals, "
            "and root-cause analysis in production environments is expected. "
            "Communication skills are important because you will write runbooks, "
            "document platform standards, and mentor engineers on resilient service "
            "ownership."
        ),
    },
    {
        "job_id": "data_engineer_001",
        "job_description": (
            "We are looking for a Data Engineer to design and maintain robust data "
            "pipelines that support analytics, reporting, and machine learning use "
            "cases. The role requires strong Python and SQL fundamentals, hands-on "
            "experience building ETL/ELT workflows, and practical knowledge of Airflow "
            "for orchestration and monitoring. You will partner with product and "
            "analytics stakeholders to model business entities, enforce data quality "
            "checks, and optimize transformation logic for cost and performance in AWS "
            "data services. The ideal candidate has experience with schema evolution, "
            "data observability, and production support for time-critical pipelines, "
            "including incident handling and postmortem follow-through. Clear "
            "documentation, testing discipline, and a focus on measurable impact are "
            "important for success in this role."
        ),
    },
    {
        "job_id": "cloud_engineer_001",
        "job_description": (
            "We are seeking a Cloud Engineer to design, automate, and operate secure "
            "and scalable cloud infrastructure across AWS environments. This role "
            "requires hands-on expertise with infrastructure-as-code using Terraform, "
            "containerized workloads with Docker, and production orchestration on "
            "Kubernetes. You will partner with application teams to improve deployment "
            "reliability, optimize cloud resource usage, and implement consistent "
            "networking and security controls across services. The position also "
            "includes building robust monitoring and alerting standards, participating "
            "in incident response rotations, and driving root-cause analysis and "
            "post-incident improvements. Strong communication and documentation skills "
            "are important, as you will create runbooks, guide engineering teams on "
            "cloud best practices, and contribute to long-term platform resilience."
        ),
    },
]


# List of EvaluationRequests (inputs)
SAMPLE_REQUESTS = [
    EvaluationRequest(
        resume_id="resume_001",
        job_id="platform_engineer_001",
        resume_text=(
            "Platform engineer with 5+ years building internal platform capabilities "
            "for backend teams. Designed and maintained Kubernetes clusters across "
            "staging and production, created standardized Helm-based deployment "
            "templates, and improved deployment safety through progressive rollout "
            "strategies. Built CI/CD pipelines in GitHub Actions with automated test "
            "gates, image scanning, and release promotion workflows. Partnered with "
            "service owners to define SLOs and introduced dashboards and alerts for "
            "latency, error rates, and saturation, reducing noisy incidents and "
            "improving MTTR. Hands-on experience with Docker image optimization, cloud "
            "infrastructure, on-call rotations, incident command, and post-incident "
            "reviews. Regularly writes runbooks and platform documentation and mentors "
            "junior engineers on reliability practices."
        ),
    ),
    EvaluationRequest(
        resume_id="resume_002",
        job_id="data_engineer_001",
        resume_text=(
            "Analytics engineer with 3 years of experience in BI reporting and "
            "warehouse modeling. Strong SQL skills for building curated tables, "
            "maintaining dashboard data models, and writing transformation queries "
            "for weekly business reviews. Has used Python for light data cleansing and "
            "validation scripts, but limited exposure to production ETL orchestration. "
            "Collaborates closely with product and operations teams to define metrics "
            "and improve reporting consistency. Familiar with data quality checks and "
            "documentation, but has not yet owned large-scale Airflow pipelines or "
            "cloud-native data platform operations."
        ),
    ),
    EvaluationRequest(
        resume_id="resume_003",
        job_id="cloud_engineer_001",
        resume_text=(
            "Customer success specialist with 6 years of experience managing enterprise "
            "accounts, onboarding users, and improving adoption through training and "
            "support playbooks. Strong communication and project coordination skills, "
            "including cross-functional planning with sales and product teams. Built "
            "customer health dashboards in spreadsheets and internal CRM tools, and "
            "led quarterly business reviews for key stakeholders. No hands-on "
            "experience with cloud infrastructure, Docker, Kubernetes, Terraform, or "
            "production incident response."
        ),
    ),
    EvaluationRequest(
        resume_id="resume_004",
        job_id="invalid_job_999",
        resume_text=(
            "Backend engineer with experience in Python APIs, SQL, and cloud services, "
            "testing how the evaluator handles unknown job IDs in the request payload."
        ),
    ),
]
