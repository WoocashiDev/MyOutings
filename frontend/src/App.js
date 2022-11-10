import './styles.css';
import Footer from "./components/Footer";
import Navbar from "./components/Navbar";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import PrivateRoute from "./utils/PrivateRoute";
import { AuthProvider } from "./context/AuthContext";
import Home from "./views/homePage";
import Login from "./views/loginPage";
import Register from "./views/registerPage";
import OutingsPage from "./views/outingsPage";
import OutingPage from "./views/outingPage";

function App() {
  return (
    <Router>
      <div className="app">
        <AuthProvider>
          <Navbar />
          <Routes>
            <Route element={
              <PrivateRoute>
                <OutingsPage/>
              </PrivateRoute>
            } path="/outings" exact />
            <Route element={
              <PrivateRoute>
                <OutingPage/>
              </PrivateRoute>
            } path="/outings/:id" exact />
            <Route element={<Login/>} path="/login" />
            <Route element={<Register/>} path="/register" />
            <Route element={<Home/>} path="/" />
          </Routes>
        </AuthProvider>
        <Footer />
      </div>
    </Router>
  );
}

export default App;
