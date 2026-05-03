import Link from "next/link";

export default function NotFound() {
  return (
    <div className="text-center p-8">
      <h2 className="text-2xl font-bold mb-4">404 - Page Not Found</h2>
      <p className="mb-4">The page you are looking for does not exist.</p>
      <Link href="/" className="text-blue-500 underline">Go Home</Link>
    </div>
  );
}
