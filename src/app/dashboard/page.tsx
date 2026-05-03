"use client";
import { useRouter } from "next/navigation";
import { useEffect, useState } from "react";

export default function DashboardPage() {
  const router = useRouter();
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  useEffect(() => {
    if (!document.cookie.includes("auth-token=logged-in")) {
      router.push("/login");
    } else {
      setIsLoggedIn(true);
    }
  }, [router]);

  const handleLogout = () => {
    document.cookie = "auth-token=; path=/; expires=Thu, 01 Jan 1970 00:00:00 GMT";
    router.push("/login");
  };

  if (!isLoggedIn) return <p>Loading...</p>;
  return (
    <div>
      <h1 className="text-2xl font-bold mb-4">Protected Dashboard</h1>
      <p className="mb-4">Welcome! You are logged in.</p>
      <button onClick={handleLogout} className="bg-red-500 text-white p-2 rounded">Logout</button>
    </div>
  );
}
