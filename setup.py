from setuptools import setup

setup(
    name="Dungeon",
    version="0.1.0",
    packages=["dungeon"],
    entry_points={
        "console_scripts": [
            "dungeon = dungeon.__main__:main"
        ]
    },
)
