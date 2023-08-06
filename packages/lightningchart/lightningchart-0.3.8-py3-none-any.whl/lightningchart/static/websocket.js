const {lightningChart} = lcjs;
const socket = io();
let log = false;
const objects = {};
const items = {};
const decoder = new TextDecoder('utf-8');
let cachedData = null;
let datas = {};

socket.on('connect', function () {
    socket.emit('join', room)
});

socket.on('message', function (data) {
    console.log(data)
});

socket.on('item', function (binary_data) {
    const item = msgpack.decode(new Uint8Array(binary_data));
    const id = item['id'];
    const command = item['command'];
    const param = item['param'];

    if (log)
        console.log('RECEIVED ITEM:', {'ID': id, 'COMMAND': command, 'PARAMETERS': param});

    if (functionLookup.hasOwnProperty(command)) {
        const func = functionLookup[command];
        const args = (typeof param === 'object') ? Object.values(param) : [];
        func(id, ...args);
    }
});

socket.on('exec', function () {
    if (cachedData)
        clearInstance()
    fetch(`/fetch_data?id=${room}`)
        .then(response => {
            if (!response.ok)
                throw new Error('Network response was not ok');
            return response.arrayBuffer();
        })
        .then(arrayBuffer => {
            const data = msgpack.decode(new Uint8Array(arrayBuffer));
            cachedData = data;
            for (let i = 1; i <= Object.keys(data).length; i++) {
                const item = data[i.toString()];
                const id = item['id'];
                const command = item['command'];
                const param = item['param'];
                if (log)
                    console.log('RECEIVED ITEM:', {'ID': id, 'COMMAND': command, 'PARAMETERS': param});
                if (functionLookup.hasOwnProperty(command)) {
                    const func = functionLookup[command];
                    const args = (typeof param === 'object') ? Object.values(param) : [];
                    func(id, ...args);
                }
            }
        })
        .then(() => {
            //console.log(Date.now() / 1000);
        })
        .catch(error => console.error(error));
});
