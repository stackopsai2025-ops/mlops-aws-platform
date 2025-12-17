#!/usr/bin/env python3
"""CDK app entrypoint"""
from aws_cdk import App
from mlops_infra.stacks.network_stack import NetworkStack


app = App()
NetworkStack(app, "mlops-network")
app.synth()
