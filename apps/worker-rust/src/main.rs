use anyhow::Result;
use tracing::info;

#[tokio::main]
async fn main() -> Result<()> {
    tracing_subscriber::fmt().with_env_filter("info").init();
    info!("foundation-worker started");
    tokio::signal::ctrl_c().await?;
    info!("foundation-worker shutting down");
    Ok(())
}
