from pytest_bdd import given, when, then

from logger import logger

@given('MTA is installed on target cluster And Contains Some Data')
def step_given_mta_installed_with_data():
    logger.info("Deploying using cypress")

@given('Backup MTA using OADP')
@when('Backup MTA using OADP')
def step_when_backup_mta_with_oadp():
    logger.info("Running Backup using OADP test framework")
    pass


@when('Remove MTA')
def step_when_remove_mta():
    logger.info("oc delete...")
    pass


@when('Restore MTA')
@when('Restore MTA using OADP')
def step_when_restore_mta_with_oadp():
    logger.info("Running Restore using oc")
    pass


@then('MTA is installed on target cluster And Contains Some Data')
def step_then_mta_installed_with_data():
    logger.info("Using api test framework to verify the mtv data")
    pass


@given('Openshift Cluster Is Deployed')
def step_given_openshift_cluster_is_installed():
    logger.info("If no cluster, deploy it.")
    pass


@given('OADP Operator is Deployed')
def step_given_openshift_cluster_is_installed():
    logger.info("If no cluster, deploy it.")
    pass