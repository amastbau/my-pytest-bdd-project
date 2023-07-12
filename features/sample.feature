Feature: Backup and Restore MTA using OADP

#  Background:
#    Given Openshift Cluster Is Deployed
#    Given OADP Operator is Deployed
#    Given DataProtectionApplication with data Native Data Mover Is Deployed

  Scenario: Backup and Restore MTA using OADP
    Given MTA is installed on target cluster And Contains Tags, Tags Type and some analysis data
    Given Some MTA Analysis are running
    Given Backup MTA using OADP
    When Remove MTA
    When Restore MTA using OADP
    Then MTA is installed on target cluster and contains all data

  Scenario Outline: Backup and Restore <app_id> with <br_flow>
      Given Application <app_id> Is Deployed Successfully
      When Backup And Restore Application <app_id> with <br_flow>
      Then Application <app_id> Is deployment is Valid.

      Examples:
      | br_flow       |  app_id       |
      | resticDM      |  ocp-mysql    |
      | kopiaNativeDM |  ocp-kubevirt |
      | restic        |  ocp-mta      |
