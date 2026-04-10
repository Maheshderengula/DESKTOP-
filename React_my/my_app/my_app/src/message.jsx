import { useState } from "react";

const Message = () => {
    const [msg, setMsg] = useState("Hello");

    const updateHandler = (value) => {
        setMsg(value);
    };

    return (
        <div>
            <h3>Message: {msg}</h3>

            <button onClick={() => updateHandler("GOOD Morning")}>
                GOOD Morning
            </button>

            <button onClick={() => updateHandler("GOOD Afternoon")}>
                GOOD Afternoon
            </button>

            <button onClick={() => updateHandler("GOOD Evening")}>
                GOOD Evening
            </button>

            <button onClick={() => updateHandler("GOOD Night")}>
                GOOD Night
            </button>
        </div>
    );
};

export default Message;