from py_logs_newrelic.push_logs import sendNewRelic


logs = sendNewRelic('https://log-api.newrelic.com/log/v1', 'f14897847369b794bef8d8b2869de57bFFFFNRAL', 'cl-jumboback-backoffice-prod', '1164762498')

logs.send_message('Error general ', 'error')
