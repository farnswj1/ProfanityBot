use std::env;

use dotenvy::dotenv;
use rustrict::CensorStr;
use serenity::all::Mentionable;
use serenity::async_trait;
use serenity::model::channel::Message;
use serenity::model::gateway::Ready;
use serenity::prelude::{Client, Context, EventHandler, GatewayIntents};
use tracing::{error, info};

struct Handler;

#[async_trait]
impl EventHandler for Handler {
    async fn message(&self, context: Context, msg: Message) {
        // Ignore all messages created by the bot itself.
        if msg.author.id == context.cache.current_user().id {
            return;
        }

        // Do nothing if the message doesn't contain profanity.
        if !msg.content.is_inappropriate() {
            return;
        }

        info!("{}: {}", msg.author.name, msg.content);
        let response = format!("Watch your mouth, {}!", msg.author.mention());
        let dm = msg.channel_id.say(&context.http, response).await;

        if let Err(error) = dm {
            error!("Error when direct messaging user: {error}");
        }
    }

    async fn ready(&self, _: Context, ready: Ready) {
        info!("{} is online!", ready.user.tag());
    }
}

#[tokio::main]
async fn main() {
    dotenv().ok();
    tracing_subscriber::fmt::init();

    let token = env::var("DISCORD_TOKEN").expect("Discord token");
    let intents = GatewayIntents::GUILD_MESSAGES
        | GatewayIntents::DIRECT_MESSAGES
        | GatewayIntents::MESSAGE_CONTENT;

    let mut client = Client::builder(&token, intents)
        .event_handler(Handler)
        .await
        .expect("Err creating client");

    if let Err(error) = client.start().await {
        error!("Client error: {error}");
    }
}
