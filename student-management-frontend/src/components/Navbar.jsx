import { useContext } from "react";
import { AuthContext } from "../context/AuthContext";
import { useNavigate } from "react-router-dom";

function Navbar() {
  const { logout } = useContext(AuthContext);
  const navigate = useNavigate();
  const handleLogout = () => {
    logout();
    navigate("/");
  }

 return (

        <nav className="navbar navbar-expand-lg navbar-dark bg-dark shadow">

            <div className="container-fluid">

                <span className="navbar-brand fw-bold">

                    🎓 Student Management

                </span>

                <button
                    className="btn btn-danger"
                    onClick={handleLogout}
                >
                    Logout
                </button>

            </div>

        </nav>

    );

}

export default Navbar;