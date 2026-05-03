export default function AboutPage() {
  return (
    <div>
      <h1 className="text-2xl font-bold mb-4">About This Demo</h1>
      <p className="mb-4">This is a simple Next.js app built to demonstrate TestSprite testing capabilities.</p>
      <p>It includes:</p>
      <ul className="list-disc pl-8 mt-2 space-y-1">
        <li>Login with test credentials</li>
        <li>Protected dashboard page</li>
        <li>Contact form with API integration</li>
        <li>Navigation across multiple pages</li>
      </ul>
    </div>
  );
}
