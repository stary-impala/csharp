using System;
using System.Diagnostics;

namespace BashRunner
{
    class Program
    {
        public static void RunBushScript(string cmd)
        {
            var process = new Process
            {
                StartInfo = new ProcessStartInfo
                {
                    FileName = "/bin/bash",
                    Arguments = $"-c \"{cmd}\"",
                    RedirectStandardInput = true,
                    RedirectStandardOutput = true,
                    RedirectStandardError = true,
                    UseShellExecute = false,
                    CreateNoWindow = true
                },
                EnableRaisingEvents = true
            };

            process.Start();
            process.BeginOutputReadLine();
            process.BeginErrorReadLine();
        }
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
        }
    }
}
