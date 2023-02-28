const input = document.getElementById("message-text");
const send_button = document.getElementById("button-send");
const messaging_area = document.getElementById("chatting-area");
const when_last_online = document.getElementById("last-online");
let user_message,user_div,chatbot_div,chatbot_message;
let notification_sound = new Audio("iphone_notification.mp3");

send_button.addEventListener("click",function(){
    message();
});

input.addEventListener("keydown",(e) =>{
    if(e.key == "Enter"){
        message();
    }
});
const message = () =>{
    user_div = document.createElement("div");
    user_message = document.createElement("p");
    user_message.textContent = input.value;
    user_div.classList.add("message-from-us");
    user_div.classList.add("message");
    let user_text = input.value;
    input.value = "";
    messaging_area.scrollTop = messaging_area.scrollHeight;
    chatbot_div = document.createElement('div');
    chatbot_message = document.createElement('p');
    chatbot_message.textContent = `The answer is ${eval(user_text)}.`;
    chatbot_div.classList.add("message-from-chatbot");
    chatbot_div.classList.add("message");
    user_div.appendChild(user_message);
    messaging_area.appendChild(user_div);
    when_last_online.textContent = "online"
    messaging_area.scrollTop = messaging_area.scrollHeight;
    setTimeout(() => {
        chatbot_div.appendChild(chatbot_message);
        messaging_area.appendChild(chatbot_div);
        notification_sound.play();
        messaging_area.scrollTop = messaging_area.scrollHeight;
    }, 1000);
}