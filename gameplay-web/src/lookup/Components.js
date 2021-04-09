import React from 'react';


function backendLookup(url, method, data2, resData) {
	let headers = ''
	let body = ''
	if (typeof data2 !== "object") {
		headers = {
        'Content-Type': 'application/json',
        Authorization: data2
      }
	} else {
		headers = {'Content-Type': 'application/json',}
		body = JSON.stringify(data2)
	}

	fetch(url, {
      method: method,
      headers: headers,
      body: body
    })
			.then(res => {
				if (res.ok) {
						return res.json()
				} else {
					return Promise.reject(`Http error: ${res.status}`);
				}
			})
			.then(res => {
				console.log(res)
				resData(res)
			})
			.catch(error => {
				console.error(error)
			})
}

export default backendLookup;