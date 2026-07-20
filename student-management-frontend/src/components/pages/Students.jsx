import { Link } from "react-router-dom";

function Students() {

    return (

        <div>

            <div className="d-flex justify-content-between">

                <h2>

                    Students

                </h2>

                <Link
                    to="/students/add"
                    className="btn btn-primary"
                >
                    Add Student
                </Link>

            </div>

            <hr />

            <table className="table table-bordered table-hover">

                <thead className="table-dark">

                    <tr>

                        <th>ID</th>

                        <th>Name</th>

                        <th>Email</th>

                        <th>Department</th>

                        <th>CGPA</th>

                        <th>Action</th>

                    </tr>

                </thead>

                <tbody>

                    <tr>

                        <td>1</td>

                        <td>John Doe</td>

                        <td>john@gmail.com</td>

                        <td>CSE</td>

                        <td>8.5</td>

                        <td>

                            <Link
                                className="btn btn-success btn-sm me-2"
                                to="/students/1"
                            >
                                View
                            </Link>

                            <Link
                                className="btn btn-warning btn-sm"
                                to="/students/edit/1"
                            >
                                Edit
                            </Link>

                        </td>

                    </tr>

                </tbody>

            </table>

        </div>

    );

}

export default Students;