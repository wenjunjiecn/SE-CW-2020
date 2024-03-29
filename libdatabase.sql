USE [master]
GO
/****** Object:  Database [libtest]    Script Date: 2019/12/21 17:23:44 ******/
CREATE DATABASE [libtest]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'libtest', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL14.SQLEXPRESS\MSSQL\DATA\libtest.mdf' , SIZE = 8192KB , MAXSIZE = UNLIMITED, FILEGROWTH = 65536KB )
 LOG ON 
( NAME = N'libtest_log', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL14.SQLEXPRESS\MSSQL\DATA\libtest_log.ldf' , SIZE = 8192KB , MAXSIZE = 2048GB , FILEGROWTH = 65536KB )
GO
ALTER DATABASE [libtest] SET COMPATIBILITY_LEVEL = 140
GO
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [libtest].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO
ALTER DATABASE [libtest] SET ANSI_NULL_DEFAULT OFF 
GO
ALTER DATABASE [libtest] SET ANSI_NULLS OFF 
GO
ALTER DATABASE [libtest] SET ANSI_PADDING OFF 
GO
ALTER DATABASE [libtest] SET ANSI_WARNINGS OFF 
GO
ALTER DATABASE [libtest] SET ARITHABORT OFF 
GO
ALTER DATABASE [libtest] SET AUTO_CLOSE ON 
GO
ALTER DATABASE [libtest] SET AUTO_SHRINK OFF 
GO
ALTER DATABASE [libtest] SET AUTO_UPDATE_STATISTICS ON 
GO
ALTER DATABASE [libtest] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO
ALTER DATABASE [libtest] SET CURSOR_DEFAULT  GLOBAL 
GO
ALTER DATABASE [libtest] SET CONCAT_NULL_YIELDS_NULL OFF 
GO
ALTER DATABASE [libtest] SET NUMERIC_ROUNDABORT OFF 
GO
ALTER DATABASE [libtest] SET QUOTED_IDENTIFIER OFF 
GO
ALTER DATABASE [libtest] SET RECURSIVE_TRIGGERS OFF 
GO
ALTER DATABASE [libtest] SET  ENABLE_BROKER 
GO
ALTER DATABASE [libtest] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO
ALTER DATABASE [libtest] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO
ALTER DATABASE [libtest] SET TRUSTWORTHY OFF 
GO
ALTER DATABASE [libtest] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO
ALTER DATABASE [libtest] SET PARAMETERIZATION SIMPLE 
GO
ALTER DATABASE [libtest] SET READ_COMMITTED_SNAPSHOT OFF 
GO
ALTER DATABASE [libtest] SET HONOR_BROKER_PRIORITY OFF 
GO
ALTER DATABASE [libtest] SET RECOVERY SIMPLE 
GO
ALTER DATABASE [libtest] SET  MULTI_USER 
GO
ALTER DATABASE [libtest] SET PAGE_VERIFY CHECKSUM  
GO
ALTER DATABASE [libtest] SET DB_CHAINING OFF 
GO
ALTER DATABASE [libtest] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO
ALTER DATABASE [libtest] SET TARGET_RECOVERY_TIME = 60 SECONDS 
GO
ALTER DATABASE [libtest] SET DELAYED_DURABILITY = DISABLED 
GO
ALTER DATABASE [libtest] SET QUERY_STORE = OFF
GO
USE [libtest]
GO
/****** Object:  Table [dbo].[Admins]    Script Date: 2019/12/21 17:23:44 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Admins](
	[adminname] [varchar](8) NOT NULL,
	[adminID] [char](12) NOT NULL,
	[passwords] [varchar](50) NOT NULL,
 CONSTRAINT [PK__Admins__AD0500866A65978B] PRIMARY KEY CLUSTERED 
(
	[adminID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Announcement]    Script Date: 2019/12/21 17:23:45 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Announcement](
	[adminID] [char](12) NOT NULL,
	[mesID] [int] IDENTITY(1244,1) NOT NULL,
	[content] [varchar](5000) NOT NULL,
	[important] [smallint] NOT NULL,
	[content_short] [varchar](500) NOT NULL,
	[author] [varchar](12) NOT NULL,
	[time] [smalldatetime] NOT NULL,
	[title] [varchar](60) NOT NULL,
 CONSTRAINT [PK__Announce__3E34524A074B4F8A] PRIMARY KEY CLUSTERED 
(
	[adminID] ASC,
	[mesID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[AT]    Script Date: 2019/12/21 17:23:45 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[AT](
	[adminID] [char](12) NOT NULL,
	[mesID] [char](12) NOT NULL,
	[content] [varchar](200) NOT NULL,
	[important] [varchar](200) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[adminID] ASC,
	[mesID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Book]    Script Date: 2019/12/21 17:23:45 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Book](
	[bookName] [varchar](20) NOT NULL,
	[author] [varchar](12) NOT NULL,
	[publisher] [varchar](20) NOT NULL,
	[ISDN] [varchar](26) NOT NULL,
	[category] [varchar](10) NOT NULL,
	[num] [int] NOT NULL,
	[addtime] [datetime] NULL,
 CONSTRAINT [PK__Book__447C84A2B4998E72] PRIMARY KEY CLUSTERED 
(
	[ISDN] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[BookMes]    Script Date: 2019/12/21 17:23:45 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[BookMes](
	[matter] [char](2) NOT NULL,
	[ISDN] [varchar](26) NOT NULL,
	[readID] [char](12) NOT NULL,
	[time] [datetime] NOT NULL,
 CONSTRAINT [PK__BookMes__6D0A42851778B1F7] PRIMARY KEY CLUSTERED 
(
	[ISDN] ASC,
	[readID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Message]    Script Date: 2019/12/21 17:23:45 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Message](
	[readID] [char](12) NOT NULL,
	[mesID] [int] IDENTITY(1,1) NOT NULL,
	[content] [varchar](400) NOT NULL,
	[addtime] [smalldatetime] NULL,
 CONSTRAINT [PK__Message__045D30BF2972C9B6] PRIMARY KEY CLUSTERED 
(
	[readID] ASC,
	[mesID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Users]    Script Date: 2019/12/21 17:23:45 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Users](
	[username] [varchar](8) NOT NULL,
	[major] [varchar](10) NOT NULL,
	[userclass] [char](4) NOT NULL,
	[readID] [char](12) NOT NULL,
	[usertype] [char](2) NOT NULL,
	[passwords] [varchar](50) NOT NULL,
 CONSTRAINT [PK__Users__976C627351EB8002] PRIMARY KEY CLUSTERED 
(
	[readID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[Book] ADD  DEFAULT (getdate()) FOR [addtime]
GO
ALTER TABLE [dbo].[Message] ADD  CONSTRAINT [DF__Message__addtime__1A69E950]  DEFAULT (getdate()) FOR [addtime]
GO
ALTER TABLE [dbo].[Announcement]  WITH CHECK ADD  CONSTRAINT [FK__Announcem__admin__57DD0BE4] FOREIGN KEY([adminID])
REFERENCES [dbo].[Admins] ([adminID])
GO
ALTER TABLE [dbo].[Announcement] CHECK CONSTRAINT [FK__Announcem__admin__57DD0BE4]
GO
ALTER TABLE [dbo].[AT]  WITH CHECK ADD  CONSTRAINT [FK__AT__adminID__7AF13DF7] FOREIGN KEY([adminID])
REFERENCES [dbo].[Admins] ([adminID])
ON UPDATE CASCADE
ON DELETE CASCADE
GO
ALTER TABLE [dbo].[AT] CHECK CONSTRAINT [FK__AT__adminID__7AF13DF7]
GO
ALTER TABLE [dbo].[BookMes]  WITH CHECK ADD  CONSTRAINT [FK__BookMes__ISDN__503BEA1C] FOREIGN KEY([ISDN])
REFERENCES [dbo].[Book] ([ISDN])
GO
ALTER TABLE [dbo].[BookMes] CHECK CONSTRAINT [FK__BookMes__ISDN__503BEA1C]
GO
ALTER TABLE [dbo].[BookMes]  WITH CHECK ADD  CONSTRAINT [FK__BookMes__readID__51300E55] FOREIGN KEY([readID])
REFERENCES [dbo].[Users] ([readID])
GO
ALTER TABLE [dbo].[BookMes] CHECK CONSTRAINT [FK__BookMes__readID__51300E55]
GO
ALTER TABLE [dbo].[Message]  WITH CHECK ADD  CONSTRAINT [FK__Message__readID__540C7B00] FOREIGN KEY([readID])
REFERENCES [dbo].[Users] ([readID])
GO
ALTER TABLE [dbo].[Message] CHECK CONSTRAINT [FK__Message__readID__540C7B00]
GO
USE [master]
GO
ALTER DATABASE [libtest] SET  READ_WRITE 
GO
