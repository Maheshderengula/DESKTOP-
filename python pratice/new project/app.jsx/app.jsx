import { useEffect, useState } from "react";
import UserTable from "./components/UserTable";
import SearchBar from "./components/SearchBar";
import Loader from "./components/Loader";

function App() {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [search, setSearch] = useState("");

  useEffect(() => {
    fetch("https://jsonplaceholder.typicode.com/users")
      .then((res) => res.json())
      .then((data) => {
        setUsers(data);
        setLoading(false);
      })
      .catch(() => setLoading(false));
  }, []);

  //  Filter users
  const filteredUsers = users.filter((user) =>
    user.name.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <div>
      <h2 style={{ textAlign: "center" }}>User Dashboard</h2>

      <SearchBar search={search} setSearch={setSearch} />

      {loading ? (
        <Loader />
      ) : (
        <UserTable users={filteredUsers} />
      )}
    </div>
  );
}

export default App;