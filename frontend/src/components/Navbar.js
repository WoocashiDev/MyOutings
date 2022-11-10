import { useContext } from "react";
import { NavLink } from "react-router-dom";
import AuthContext from "../context/AuthContext";

const Navbar = () => {
  const { user, logoutUser } = useContext(AuthContext);
  return (
      <div className="container">
        <nav className="nav">
          <span className="nav-logo">MyOutings</span>
          <div>
            {user ? (
              <div className="nav-links">
                <NavLink className={({isActive})=>isActive?"active nav-link":"nav-link"} to="/">Home</NavLink>
                <NavLink className={({isActive})=>isActive?"active nav-link":"nav-link"} to="/outings">Outings</NavLink>
                <button className="nav-button" onClick={logoutUser}>Logout</button>
              </div>
            ) : (
              <div className="nav-links">
                <NavLink className={({isActive})=>isActive?"active nav-link":"nav-link"} to="/login">Login</NavLink>
                <NavLink className={({isActive})=>isActive?"active nav-link":"nav-link"} to="/register">Register</NavLink>
              </div>
            )}
          </div>
          </nav>
        </div>
  );
};

export default Navbar;