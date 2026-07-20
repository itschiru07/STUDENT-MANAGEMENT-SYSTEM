import { NavLink } from "react-router-dom";

function Sidebar() {

    return (

        <div className="sidebar p-3">

            <h4 className="text-white mb-4">

                Dashboard

            </h4>

            <NavLink
                to="/dashboard"
                className="nav-link mb-2"
            >
                🏠 Dashboard
            </NavLink>

            <NavLink
                to="/students"
                className="nav-link mb-2"
            >
                👨‍🎓 Students
            </NavLink>

            <NavLink
                to="/students/add"
                className="nav-link mb-2"
            >
                ➕ Add Student
            </NavLink>

            <NavLink
                to="/profile"
                className="nav-link mb-2"
            >
                👤 Profile
            </NavLink>

        </div>

    );

}

export default Sidebar;