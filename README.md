# Logz.io Host Metrics Collector

Logz.io Host Metrics Collector is a Docker container that forwards system metrics from its host to your Logz.io account.

To use this container, you'll set environment variables in your docker run command.
Host Metrics Collector uses those environment variables to generate a valid Metricbeat configuration for the container.

By default, Host Metrics Collector ships these metrics: \
`cpu`, `diskio`, `filesystem`, `fsstat`, `load`, `memory`, `network`, `process_summary`, `process`, `process`, `raid`, `socket_summary`, `socket`, `uptime`

## Setup

### 1. Pull the Docker image

Download the logzio/host-metrics-collector image:

```shell
docker pull logzio/host-metrics-collector
```

### 2. Run the Docker image

For a complete list of options, see the parameters below the code block.👇

```shell
docker run --name host-metrics-collector \
--env LOGZIO_TOKEN="<ACCOUNT-TOKEN>" \
--env LOGZIO_URL="<LISTENER-URL>:5015" \
logzio/host-metrics-collector
```

#### Parameters

| Parameter | Description |
|---|---|
| **LOGZIO_TOKEN** | **Required**. Your Logz.io account token. Replace `<ACCOUNT-TOKEN>` with the [token](https://app.logz.io/#/dashboard/settings/general) of the account you want to ship to. |
| **LOGZIO_URL** | **Required**. Logz.io listener URL to ship the metrics to. This URL changes depending on the region your account is hosted in. For example, accounts in the US region ship to `listener.logz.io`, and accounts in the EU region ship to `listener-eu.logz.io`. <br /> For more information, see [Account region](https://docs.logz.io/user-guide/accounts/account-region.html) on the Logz.io Docs. |
| **HOSTNAME** | Custom name of the host. <br /> **Default**: `HOSTNAME` environment variable

### 3. Check Logz.io for your metrics

Give your metrics some time to get from your system to ours, and then open [Kibana](https://app.logz.io/#/dashboard/kibana).
For full description of the collected metrics, see [Metricbeat documentation](https://www.elastic.co/guide/en/beats/metricbeat/current/exported-fields-system.html).
