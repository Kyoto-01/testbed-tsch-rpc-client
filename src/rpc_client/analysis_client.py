import requests


class TestbedDataAnalysisRPCClient:

    def __init__(
        self,
        testbedName: 'str',
        apiAddr: 'str' = '127.0.0.1',
        apiPort: 'int' = 5000
    ):
        self._testbedName = testbedName
        self._url = f'http://{apiAddr}:{apiPort}'

    def _treat_procedure_response(
        self,
        response: 'dict'
    ):
        status = response.status_code
        time = response.elapsed

        if status == 200:
            response = response.json()
        else:
            response = {}

        response['status'] = status
        response['time'] = time

        return response

    def _exec_procedure(
        self,
        uri: 'str',
        body: 'dict'
    ) -> 'dict':
        uri = f'{self._url}{uri}'

        headers = {
            'Content-Type': 'application/json'
        }

        res = requests.get(
            url=uri,
            headers=headers,
            json=body
        )

        res = self._treat_procedure_response(res)

        return res

    def exec_all_analysis(
        self,
        txOffset: 'dict' = {}
    ) -> 'dict':
        uri = '/rpc/analysis/update/all'

        body = {
            'testbed_name': self._testbedName,
            'tx_offset': txOffset
        }

        res = self._exec_procedure(uri, body)

        return res
