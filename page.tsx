export default function Home() {
  return (
    <div>
      <h1 className="text-3xl font-bold mb-4 text-red-500">Welcome to TestSprite Demo</h1>
      <p className="mb-4">This app is designed to test all TestSprite features including:</p>
      <ul className="list-disc pl-8 space-y-2">
        <li>Authentication flows (Login/Logout)</li>
        <li>Form validation and submission</li>
        <li>API routes (GET and POST)</li>
        <li>Protected pages (Dashboard)</li>
        <li>Navigation and routing</li>
        <li>Error handling and 404 pages</li>
      </ul>
    </div>
  );
}
