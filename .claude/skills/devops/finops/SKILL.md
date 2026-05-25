---
name: finops
description: Cloud FinOps cost optimization
category: devops
tags: [finops, cloud-cost, optimization, aws, azure, gcp]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# FinOps

> Implement cloud financial operations for cost visibility, optimization, and governance.

## Quick Start
```python
# AWS cost analysis with boto3
import boto3
from datetime import datetime, timedelta

ce = boto3.client('ce')

def get_daily_costs(days: int = 30) -> list:
    response = ce.get_cost_and_usage(
        TimePeriod={
            'Start': (datetime.now() - timedelta(days=days)).strftime('%Y-%m-%d'),
            'End': datetime.now().strftime('%Y-%m-%d')
        },
        Granularity='DAILY',
        Metrics=['UnblendedCost', 'UsageQuantity'],
        GroupBy=[
            {'Type': 'DIMENSION', 'Key': 'SERVICE'},
            {'Type': 'DIMENSION', 'Key': 'REGION'}
        ]
    )
    return response['ResultsByTime']

def tag_compliance_report() -> dict:
    """Report resources missing required cost-center tags"""
    tag_key = "CostCenter"
    required_tags = ["engineering", "marketing", "data", "infra"]
    
    # Find untagged resources
    resource_groups = boto3.client('resource-explorer-2')
    # (Implementation depends on resource type)
    return {"untagged_count": 0, "estimated_waste": 0}

# Budget alert setup
budgets = boto3.client('budgets')
budgets.create_budget(
    AccountId='123456789012',
    Budget={
        'BudgetName': 'monthly-infra',
        'BudgetLimit': {'Amount': '50000', 'Unit': 'USD'},
        'CostFilters': {'TagKeyValue': ['CostCenter$engineering']},
        'CostTypes': {'IncludeTax': True},
        'TimeUnit': 'MONTHLY',
        'BudgetType': 'COST'
    },
    NotificationsWithSubscribers=[{
        'Notification': {
            'NotificationType': 'ACTUAL',
            'ComparisonOperator': 'GREATER_THAN',
            'Threshold': 80,
            'ThresholdType': 'PERCENTAGE'
        },
        'Subscribers': [{'Address': 'team@example.com', 'SubscriptionType': 'EMAIL'}]
    }]
)
```

## Key Concepts
FinOps has three phases: Inform (visibility), Optimize (efficiency), Operate (continuous improvement). Track unit economics (cost per customer/feature). Use tagging, budgets, reserved instances, and right-sizing.

## When to Use
- Cloud spend is growing faster than business metrics
- Teams lack visibility into resource costs
- Need to attribute costs to teams or features
- Implementing showback/chargeback models

## Validation
1. Cost reports show costs broken down by service, team, and environment
2. Budget alerts trigger at configured thresholds
3. Tag compliance > 90% across all resources
4. Rightsizing recommendations reduce compute costs by 15%+
