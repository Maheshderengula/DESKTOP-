import { useState } from "react";


const [form, setForm] = useState({
   let[upperCase, setUpperCase] = useState(false)
   let[lowerCase, setLowerCase] = useState(false)
   let[number, setNumber] = useState(false)  
});

function handleChange(e) {          

    setForm({

        ...form,
        [e.target.name]: e.target.value
    });
}


export default function Login() {

    return (
        <div className="container">

            <h1 className="text-center mt-5">Login</h1>
            <form className="w-50 mx-auto mt-5">
                <div className="mb-3">
                    <label htmlFor="email" className="form-label">Email address</label>
                    <input type="email" className="form-control" id="email" name="email" onChange={handleChange} />
                </div>
                <div className="mb-3">
                    <label htmlFor="password" className="form-label">Password</label>

                    <input type="password" className="form-control" id="password" name="password" onChange={handleChange} />
                </div>
                <button type="submit" className="btn btn-primary">Submit</button>
            </form>
        </div>
    );
}   