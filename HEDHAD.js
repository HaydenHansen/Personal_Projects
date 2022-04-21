console.log('Beep beep!')

const Discord = require('discord.js');
const client = new Discord.Client();
client.login('<your discord token here');

client.on('ready', readyDiscord);

function readyDiscord() {
    console.log('Connectedarooski')
}

client.on('message', gotMessage);

function gotMessage(msg) {
    console.log(msg.content);
    if (msg.content === 'HEDHAD what do you think of Hayden'){
        msg.reply('Cool dude');
    }
    else if (msg.content === 'HEDHAD what do you think of Drake'){
        msg.channel.send('Hate that dude');
    }
    else if (msg.content === 'test'){
        msg.author.send('Hi');
    }
}
