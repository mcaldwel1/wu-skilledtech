var request = require('request');

request.get(
    'https://www.wu-skilledtech.com/admin/api/v2/assessments/65cd2be39bc1aed0e6001d2b/responses',
    { json: { key: 'value' } },
    function (error, response, body) {
        if (!error && response.statusCode == 200) {
            console.log(body);
        }
        else {
            console.error('error', response.body);
            console.log('statusCode:', response && response.statusCode);
        }
    }
);