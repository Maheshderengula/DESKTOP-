import React, { useState } from 'react'
const Login = () => {
  let [user,setUser] = useState({"email":"",password:""})
  let updateForm = (event)=>{
    setUser({...user,[event.target.name]:event.target.value})
  }
  return <div>
            <h3>Form Component</h3><hr/>
            <pre>{JSON.stringify(user)}</pre>
            <form>
    Email:::::::: <input type="email" name="email" onChange={updateForm}/>  <br/><br/>
    Password: <input type="password" name="password" onChange={updateForm} /> <br/><br/>
               <input type="submit" value="Login" />
            </form>
        </div>
}
export default Login