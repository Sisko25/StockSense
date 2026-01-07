export default async (request, context) => {
  const response = await context.next();
  const deepseekKey = context.env.DEEPSEEK_KEY || "";
  const polygonKey = context.env.POLYGON_KEY || "";

  const script = `
    <script>
      window.configKeys = {
        "DEEPSEEK_KEY": "${deepseekKey}",
        "POLYGON_KEY": "${polygonKey}"
      };
    </script>
  `;

  // Inject the script before the closing </head> tag
  return new HTMLRewriter()
    .on("head", {
      element(element) {
        element.append(script, { html: true });
      },
    })
    .transform(response);
};