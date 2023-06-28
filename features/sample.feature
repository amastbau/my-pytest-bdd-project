Feature: Backup and Restore MTA using OADP

  Background:
    Given Openshift Cluster Is Deployed
    Given OADP Operator is Deployed
    Given DataProtectionApplication with data Native Data Mover Is Deployed

  Scenario: Backup and Restore MTA using OADP
    Given MTA is installed on target cluster And Contains Tags, Tags Type and some analysis data
    Given MTA Analysis are running
    Given Backup MTA using OADP
    When Remove MTA
    When Restore MTA using OADP
    Then MTA is installed on target cluster and contains all data

