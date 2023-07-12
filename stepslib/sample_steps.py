import logging

from pytest_bdd import scenarios, given, then

# Define scenarios
scenarios('../features/sample.feature')

logger = logging.getLogger()

@given('MTA is installed on target cluster And Contains Tags, Tags Type and some analysis data')
def step_given_mta_installed_with_data():
    logger.info("MTA is installed on target cluster And Contains Tags, Tags Type and some analysis data")
    pass

@given('Some MTA Analysis are running')
def step_given_openshift_cluster_is_installed():
    logger.info("Some MTA Analysis are running")
    pass


@given('Some MTA Analysis are running')
def step_given_openshift_cluster_is_installed():
    logger.info("ome MTA Analysis are running.")
    pass

@given('Remove MTA')
def step_given_openshift_cluster_is_installed():
    logger.info("Remove MTA.")
    pass

@given('Restore MTA using OADP')
def step_given_openshift_cluster_is_installed():
    logger.info("Restore MTA using OADP")
    pass


@given('MTA is installed on target cluster and contains all data')
@then('MTA is installed on target cluster and contains all data')
def step_given_openshift_cluster_is_installed():
    logger.info("MTA is installed on target cluster and contains all data")
    pass


