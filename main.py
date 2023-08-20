import discord
import random
import asyncio

# Your bot's token
TOKEN = ''

# ID of the target server and channel
SERVER_ID = 123456
CHANNEL_ID = 123456

# List of random messages
random_messages = [
    "Hello, world!",
    "How's everyone doing?",
    "Just dropping by to say hi!",
    "Hope you're having a great day!",
    "Keep shining bright!",
    "Smile and spread positivity!",
    "You're capable of amazing things!",
    "Sending good vibes your way!",
    "Believe in yourself and your dreams.",
    "You're unique and wonderful!",
    "Every day is a new opportunity.",
    "You're making a difference!",
    "Embrace the journey of life.",
    "You're stronger than you think!",
    "Today is full of possibilities.",
    "You're a ray of sunshine!",
    "Chase your dreams with passion.",
    "You're valued and appreciated.",
    "Stay positive and keep moving forward.",
    "The world is better with you in it.",
    "You're capable of overcoming anything.",
    "Your kindness makes a difference.",
    "Keep your head high and stay strong.",
    "You're doing better than you know.",
    "Your potential is limitless!",
    "Spread kindness and positivity.",
    "Believe in the power of positivity.",
    "You're a true inspiration.",
    "Keep smiling and keep shining.",
    "You're making progress every day.",
    "You bring joy to those around you.",
    "Keep pushing through challenges.",
    "You're meant for great things!",
    "Your positivity is contagious.",
    "Take pride in your accomplishments.",
